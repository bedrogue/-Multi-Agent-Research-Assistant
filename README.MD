# 🔬 Multi-Agent Research Assistant

A smart AI tool that researches any topic for you automatically. Just type a topic and it searches the web, reads articles, writes a full report, and gives feedback — all on its own.

---

## 🤖 What It Does

You type a topic like **"Narendra Modi"** or **"Climate Change"** and the system does everything automatically:

| Step | Agent | What It Does |
|------|-------|-------------|
| 1 | 🔍 Search Agent | Searches the web for recent info using Tavily |
| 2 | 📄 Reader Agent | Opens the best article and reads the full content |
| 3 | ✍️ Writer Chain | Writes a structured report with intro, findings, and conclusion |
| 4 | ⭐ Critic Chain | Reviews the report and gives a score out of 10 |

---

## 🛠️ Built With

| Tool | What It Does |
|------|-------------|
| 🟣 Groq | Fast AI model (llama-3.3-70b) |
| 🔗 LangChain | Connects AI with tools and prompts |
| 🕸️ LangGraph | Runs and manages the agents |
| 🌐 Tavily | Searches the web in real time |
| 🍜 BeautifulSoup | Scrapes and reads website content |
| 🎨 Streamlit | The beautiful UI you interact with |
| ⚡ FastAPI | REST API backend |

---

## 📸 Features

- 🎨 Beautiful light lavender UI
- 💡 Example topic buttons for quick start
- 📊 Live progress bar while agents are running
- 📥 Download your research report as a `.txt` file
- ⭐ Automatic report scoring with strengths and weaknesses
- 🔌 REST API with Swagger docs at `/docs`

---

## ⚙️ Setup Guide

**Step 1 — Clone the project**
```bash
git clone https://github.com/bedrogue/multi-agent-research.git
cd multi-agent-research
```

**Step 2 — Create a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

**Step 3 — Install all packages**
```bash
pip install -r requirements.txt
```

**Step 4 — Create your `.env` file**

Create a `.env` file inside the `app/` folder:
```
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

**Step 5 — Run the app**
```bash
streamlit run app/streamlit_app.py
```
Open your browser at **http://localhost:8501**

---

## 🔑 Get Free API Keys

**Groq** → https://console.groq.com → Sign up → API Keys → Create new key

**Tavily** → https://tavily.com → Sign up → Copy key from dashboard

---

## 📁 Project Structure

```
multi-agent-research/
│
├── app/
│   ├── agents.py          → AI model, agents, writer and critic chains
│   ├── pipeline.py        → Connects all 4 agents together
│   ├── tool1.py           → Web search and scraping tools
│   ├── streamlit_app.py   → The UI you see in the browser
│   ├── app.py             → FastAPI backend
│   ├── schema.py          → API request and response format
│   └── .env               → Your secret API keys (never share this!)
│
├── requirements.txt       → All Python packages needed
└── README.md              → This file
```

---

## 💡 How to Use

1. Open the app in your browser
2. Type any topic in the search box
3. Or click one of the example buttons below the input
4. Click **🚀 Research**
5. Watch the progress bar as each agent works
6. Read your report and download it!

---

## 🔌 API Usage

Run the API:
```bash
uvicorn app.app:app --reload
```

Test at **http://localhost:8000/docs**

Example request:
```bash
curl -X POST "http://localhost:8000/research" \
     -H "Content-Type: application/json" \
     -d '{"topic": "Narendra Modi"}'
```

---


---

## 📦 Requirements

```
streamlit
langchain
langchain-groq
langchain-core
langgraph
tavily-python
beautifulsoup4
requests
python-dotenv
fastapi
uvicorn
pydantic
```

---

## 🙌 Credits

- [Groq](https://groq.com) — Lightning fast LLM inference
- [LangChain](https://langchain.com) — LLM framework
- [LangGraph](https://langchain-ai.github.io/langgraph) — Agent framework
- [Tavily](https://tavily.com) — AI-optimized search API
- [Streamlit](https://streamlit.io) — Python UI framework

---

Made with ❤️ by Lakshit
