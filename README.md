# LLM Agent System

A modular AI agent system built using **Azure OpenAI (GPT-4o)** with tool execution, persistent memory, and a FastAPI web interface.

This project demonstrates how to design and build an intelligent LLM-powered agent with a clean modular architecture suitable for production-level AI applications.

---

##  Features

- Azure OpenAI integration (GPT-4o / GPT models)
- Tool-calling system (calculator + extensible tools)
- Persistent memory system (conversation history stored locally)
- FastAPI web interface for browser interaction
- Modular and scalable agent architecture
- Environment-based configuration using `.env`
- Lightweight JSON-based storage system

---

## Project Structure
lm-agent-system/
│
├── app/
│ ├── agent/
│ │ ├── core.py # Main reasoning engine
│ │ ├── executor.py # Tool execution handler
│ │
│ ├── memory/
│ │ ├── memory_store.py # Load/save memory logic
│ │
│ ├── services/
│ │ ├── openai_client.py # Azure OpenAI client setup
│ │
│ ├── tools/
│ │ ├── calculator.py # Math tool
│ │ ├── registry.py # Tool registry system
│ │
│ ├── prompts/
│ │ ├── system_prompt.txt # System instructions for agent
│ │
│ ├── static/
│ │ ├── index.html # Web UI frontend
│ │
│ ├── web.py # FastAPI server
│ ├── main.py # CLI entry point
│ ├── config.py # Configuration loader
│
├── tests/
│ ├── test_agent.py # Basic tests
│
├── memory.json # Persistent memory storage
├── profile.json
├── requirements.txt
├── .env
├── .gitignore
└── README.md


---

##  Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/Ghayas0772/llm-agent-system
cd llm-agent-system

2. Create Virtual Environment
python -m venv venv
Activate:
Windows:
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables
Create a .env file:
AZURE_OPENAI_API_KEY=your_api_keyAZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/AZURE_OPENAI_DEPLOYMENT=gpt-4o-5AZURE_OPENAI_API_VERSION=2024-12-01-preview

5. Run CLI Agent
python -m app.main

6. Run Web Interface
uvicorn app.web:app --reload
Open in browser:
http://127.0.0.1:8000

 How It Works


User sends input (CLI or web interface)


Agent loads previous memory


Agent decides whether tools are needed


Azure OpenAI generates response


Memory is updated and stored locally



Tools System
The agent supports modular tools:


Calculator tool for mathematical operations


Registry system for adding new tools


Extensible architecture for future tools (web search, file reader, etc.)



 Memory System


Stores conversation history in memory.json


Loads previous context for continuity


Keeps only last 10 messages for performance and cost control



🌐 Web Interface
Built using FastAPI:


Simple HTML UI


Input box for queries


Real-time AI responses


API endpoint: /chat



 Example Usage
You: 12 * 4Agent: 48You: My name is GhayasAgent: Nice to meet you, Ghayas.You: What is my name?Agent: Your name is Ghayas.

Technologies Used


Python


Azure OpenAI (GPT-4o)


FastAPI


JavaScript (frontend)


JSON (memory storage)



Future Improvements


Function calling (real structured tool execution)


Vector database memory (FAISS / Pinecone)


Multi-agent system design


Azure App Service deployment (live URL)


Authentication system



Author
Ghayasudin Ghayas


AI / ML Engineer


Data Scientist


Azure OpenAI & LLM Systems Developer



📄 License
This project is for educational and research purposes.

