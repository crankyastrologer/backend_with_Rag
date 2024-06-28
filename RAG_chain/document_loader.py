from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma


from .embedding import embeddings

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def document_loader():
    loader = DirectoryLoader("new_data", glob="*.txt")
    docs = loader.load()
    docs_texts = [d.page_content for d in docs]
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    vectorstore = Chroma.from_documents(documents=splits,embedding=embeddings)
    return [vectorstore,format_docs]