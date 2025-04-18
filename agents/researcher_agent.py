from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

llm = Ollama(model="mistral")

research_prompt = PromptTemplate.from_template(
    "You are a research planner. Given a question, write a short plan on what to search or analyze.\nQuestion: {query}"
)

def researcher_agent(query):
    chain = research_prompt | llm
    return chain.invoke({"query": query})
