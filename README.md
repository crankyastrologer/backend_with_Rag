# Resume Question/Answer chatbot API

This is a simple api server made to provide ragchain to companion app it basically creates a ragchain on a given data 
and model and serves as the interface between the llm and the frontend where the user will ask the questions
<br>
Right now it is using fairly simple ragchain with RAPTOR but idea is to make it more sophesticated with time to support 
better generation.
<br>
Along with this is a simple scraper to scrape repositories of readme files

## Tech Stack
- [Lang Chain](https://www.langchain.com/)
- [Gemini](https://gemini.google.com/app?hl=en-IN)
- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)
- [Cloudflare](https://ai.cloudflare.com/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)