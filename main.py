from agents.researcher_agent import researcher_agent
from agents.summarizer_agent import summarizer_agent
from agents.evaluator_agent import evaluator_agent

def run_pipeline(query):
    print("[+] Starting Multi-Agent Pipeline\n")

    research_plan = researcher_agent(query)
    print(f"[Researcher Agent]: {research_plan}\n")

    # Mocked content as if it were fetched from the web
    simulated_results = """
    LangChain is an open-source framework designed to simplify the creation of applications using large language models (LLMs). It provides tools for chaining together multiple LLM calls and integrating them with external data sources.
    """

    summary = summarizer_agent(simulated_results)
    print(f"[Summarizer Agent]: {summary}\n")

    final_eval = evaluator_agent(summary)
    print(f"[Evaluator Agent]: {final_eval}\n")

if __name__ == '__main__':
    user_query = "What is LangChain and why is it useful?"
    run_pipeline(user_query)
