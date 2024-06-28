import requests
from bs4 import BeautifulSoup
import os

# Function to get the list of repositories
def get_repos(username):
    url = f"https://github.com/{username}?tab=repositories"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch repositories for user: {username}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    repos = soup.find_all('a', itemprop='name codeRepository')
    return [repo.text.strip() for repo in repos]

# Function to get the README content of a repository
def get_readme(username, repo):
    url = f"https://raw.githubusercontent.com/{username}/{repo}/main/README.md"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

# Main function
def main(username):
    repos = get_repos(username)
    if not repos:
        return

    if not os.path.exists('readmes'):
        os.makedirs('readmes')

    for repo in repos:
        readme_content = get_readme(username, repo)
        if readme_content:
            with open(f'readmes/{repo}_README.md', 'w', encoding='utf-8') as file:
                file.write(readme_content)
            print(f"Saved README for repository: {repo}")
        else:
            print(f"No README found for repository: {repo}")

if __name__ == "__main__":
    github_username = "crankyastrologer"
    main(github_username)
