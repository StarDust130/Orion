# 🗺️ Roadmap

| Status | Phase | What You'll Build |
|:------:|:------|:------------------|
| ✅ | **Phase 0** | Project Foundation |
| ✅ | **Phase 1** | Minimal AI Backend<br>└── `/chat` works |
| ✅ | **Phase 2** | Prompt System<br>└── Better prompts |
| ⏭️ | **Phase 3** | Structured Outputs<br>└── Skip for now<br>└── Used later for Tool Calling & Agents |
| ✅ | **Phase 4** | Conversation Memory<br>└── **Next** |
| ⬜ | **Phase 5** | Streaming<br>└── ChatGPT typing effect |
| ⬜ | **Phase 6** | Tool Calling<br>└── Calculator<br>└── Weather<br>└── Search |
| ⬜ | **Phase 7** | MCP<br>└── External tools |
| ⬜ | **Phase 8** | RAG<br>└── Documents<br>└── Vector DB |
| ⬜ | **Phase 9** | Agent<br>└── Planning<br>└── Multi-step reasoning |
| ⏭️ | **Phase 10** | Authentication |
| ⬜ | **Phase 11** | Guardrails |
| ⏭️ | **Phase 12** | Caching |
| ⏭️ | **Phase 13** | Observability |
| ⬜ | **Phase 14** | Cost Tracking |
| ⏭️ | **Phase 15** | Evaluation |
| ⏭️ | **Phase 16** | Deployment |
| ⬜ | **Phase 17** | Production Architecture |
| ⏭️ | **Phase 18** | Scaling |
| ⬜ | **Phase 19** | Production Hardening |
| ⬜ | **Phase 20** | **Orion v1 🚀** |

---

# 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| 🐍 Language | Python |
| ⚡ Backend | FastAPI |
| 🤖 LLM Providers | OpenAI • Anthropic • Groq |
| 🧠 AI Framework | LangGraph |
| 🔌 Protocol | MCP |
| 📚 Knowledge Base | Vector Database |
| 🗄️ Database | PostgreSQL |
| 🚀 Containerization | Docker |
| ☁️ Deployment | Cloud Platforms |
| 📊 Monitoring | Logging & Observability |

> **Goal:** Build an AI backend using the same concepts and architecture used in production systems.

---

#### ⭐ Express.js vs FastAPI Comparison

| **Express.js** | **FastAPI** | **What it does** |
| :------------- | :---------- | :--------------- |
| `Express()` | `FastAPI()` | Create the app |
| `Route` | `Path Operation` | Define an endpoint |
| `Controller` | `APIRouter` | Organize routes |
| `Middleware` | `Middleware` | Run code before/after requests |
| `Service` | `Service` | Business logic |
| `dotenv` | `Pydantic Settings` | Load environment variables |
| `Axios` | `httpx` | Make HTTP requests |
| `express.json()` | Automatic Request Parsing | Read JSON request body |
| `Zod` | `Pydantic Model` | Validate request data |
| `req.body` | Function parameter (`user: User`) | Access request data |
| `process.env` | `settings` | Read environment variables |
| `npm` | `pip` | Install packages |
| `package.json` | `pyproject.toml` | Project configuration |

---

## 🎯 What You'll Build

- ✅ Production-ready AI Backend
- ✅ Prompt Engineering
- ✅ Structured Outputs
- ✅ Streaming Responses
- ✅ Tool Calling
- ✅ Memory
- ✅ RAG
- ✅ MCP
- ✅ AI Agents
- ✅ Authentication
- ✅ Guardrails
- ✅ Caching
- ✅ Logging & Monitoring
- ✅ Cost Tracking
- ✅ Evaluation
- ✅ Deployment
- ✅ Production Scaling
- ✅ Real-world AI Architecture