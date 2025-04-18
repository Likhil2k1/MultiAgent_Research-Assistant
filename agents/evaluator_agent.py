from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

llm = Ollama(model="mistral")

eval_prompt = PromptTemplate.from_template(
    "Evaluate this summary for clarity and completeness. If anything is missing, suggest improvements:\n{summary}"
)

def evaluator_agent(summary):
    chain = eval_prompt | llm
    return chain.invoke({"summary": summary})
