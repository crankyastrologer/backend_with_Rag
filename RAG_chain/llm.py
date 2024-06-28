from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from .document_loader import document_loader


def load():
    llm = ChatGoogleGenerativeAI(model='gemini-pro')
    vectorstore, format_docs = document_loader()
    retriever = vectorstore.as_retriever(search_kwargs={'k': 6})
    prompt = PromptTemplate(
        template="""You are an assistant for question-answering tasks regarding ansh's abilities. Use the following pieces of retrieved context about ansh  to answer the question. If you don't know the answer, just say that you don't know. The answer should be detailed.\nQuestion: {question} \nContext: {context} \nAnswer:""",
        input_variables=['context', 'question'])
    rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
    )
    return rag_chain

def getResponse(question,rag_chain):

    ans = rag_chain.invoke(question)
    return ans;