from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from agent.retriever import load_retriever
import os

def run_agent(query):
    retriever = load_retriever()
    llm = ChatOpenAI(temperature=0.3, model="gpt-3.5-turbo")
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    result = qa.run(query)
    return result

