# 🧠 Multi-Agent Research Assistant (Offline LangChain + Ollama)

This project showcases a **fully offline, multi-agent system** using [LangChain](https://www.langchain.com/) and [Ollama](https://ollama.com/) with the **Mistral** language model.

## 🔧 What It Does
- **Researcher Agent:** Plans what needs to be searched or analyzed
- **Summarizer Agent:** Summarizes mock (or real) content
- **Evaluator Agent:** Checks summary quality and recommends improvements

## 🖥 How to Run
### 1. Install Ollama and Pull a Model
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull mistral
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Project
```bash
python main.py
```

## 📂 Project Structure
```
multi_agent_research_assistant/
├── main.py
├── agents/
│   ├── researcher_agent.py
│   ├── summarizer_agent.py
│   └── evaluator_agent.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 📌 Ideal For
- Resume portfolio
- AI pipeline showcase
- LangChain & Ollama offline demos

---

Built with 💡 by **Likhil Penujuli**
