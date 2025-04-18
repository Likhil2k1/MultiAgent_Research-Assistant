from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

llm = Ollama(model="mistral")

summary_prompt = PromptTemplate.from_template(
    "You are a summarizer. Read the following information and write a concise 3-line summary:\n{content}"
)

def summarizer_agent(content):
    chain = summary_prompt | llm
    return chain.invoke({"content": content})
