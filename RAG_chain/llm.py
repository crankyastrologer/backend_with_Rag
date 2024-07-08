from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from .document_loader import document_loader
from langchain_community.llms.cloudflare_workersai import CloudflareWorkersAI
import os
def load():
    llm = CloudflareWorkersAI(account_id=os.environ['ACCOUNT_ID'],api_token = os.environ['API_TOKEN'],model='@cf/qwen/qwen1.5-14b-chat-awq')
    vectorstore, format_docs = document_loader()
    retriever = vectorstore.as_retriever(search_kwargs={'k': 6})
    prompt = PromptTemplate(
        template="""[INST]<<SYS>> You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise. Answer in a natural way like a human would and dont mention that you retreived it from context<</SYS>> 
Question: {question} 
Context: {context} 
Answer: [/INST]""",
        input_variables=['context', 'question'])
    print(llm.model)
    print(prompt.template)
    rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
    )
    return rag_chain

def getResponse(question,rag_chain):

    ans = rag_chain.invoke(question)
    print(ans)
    return ans