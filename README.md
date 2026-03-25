# ✍️ Multi-Agent AI Writing System

An intelligent **multi-agent content generation system** inspired by modern agent architectures.
This project simulates a real-world AI workflow where different agents collaborate to produce high-quality written content.

---

## 🚀 Overview

This application uses a **multi-step agent pipeline**:

1. **Planner Agent** → Creates a structured outline
2. **Writer Agent** → Generates full content
3. **Editor Agent** → Refines and improves the output

The system mimics advanced agent frameworks (like LangGraph) but is simplified using OpenAI APIs for easy deployment.

---

## 🧠 Architecture

```
User Input
   ↓
Planner Agent (Outline Generation)
   ↓
Writer Agent (Content Creation)
   ↓
Editor Agent (Refinement & Polishing)
   ↓
Final Output
```

Each agent performs a specialized task, improving the overall quality and structure of the generated content.

---

## ✨ Features

* 🧩 Multi-agent workflow (planner, writer, editor)
* ⚡ Fast and lightweight (no AWS dependency)
* 🌐 Streamlit-based interactive UI
* 🎯 Customizable prompts and content style
* 🔐 Secure API key handling using `.env`
* 🚀 Easy deployment on cloud platforms

---

## 📁 Project Structure

```
writing-agent/
│
├── application/
│   └── app.py              # Streamlit UI
│
├── agents/
│   ├── planner.py          # Planning agent
│   ├── writer.py           # Writing agent
│   └── editor.py           # Editing agent
│
├── utils/
│   └── llm.py              # OpenAI helper
│
├── .env                    # API keys (not pushed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/writing-agent.git
cd writing-agent
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

#### Activate:

**Mac/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Setup

This project uses the OpenAI API from OpenAI.

### Steps:

1. Go to: https://platform.openai.com/api-keys
2. Create a new API key
3. Create a `.env` file in root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

⚠️ **Important:** Never commit `.env` to GitHub.

---

## ▶️ Running the Application

```bash
streamlit run application/app.py
```

Open in browser:

```
http://localhost:8501
```

---

## ☁️ Deployment

### 🚀 Deploy on Railway

You can deploy easily on Railway:

1. Push your code to GitHub
2. Go to Railway → New Project
3. Deploy from GitHub
4. Add environment variable:

```
OPENAI_API_KEY=your_key_here
```

5. Set start command:

```bash
streamlit run application/app.py --server.port $PORT --server.address 0.0.0.0
```

---

### 🌍 Alternative Platforms

* Render
* Vercel (frontend only)

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **LLM:** OpenAI GPT models
* **Environment:** python-dotenv

---

## 💡 Use Cases

* Blog generation
* Essay writing
* Content ideation
* Academic assistance
* Marketing copywriting

---

## 🔒 Security Best Practices

* Never expose your API key
* Always use `.env` for secrets
* Regenerate keys if leaked

---

## 📌 Future Improvements

* 🧠 Add memory (chat history)
* 🌐 Integrate web search tools
* 🎨 Improve UI/UX design
* 📄 Export content as PDF
* 🤖 Implement full LangGraph workflow

---

## 🏆 Resume Value

This project demonstrates:

* Multi-agent system design
* Prompt engineering
* API integration
* Full-stack deployment

You can describe it as:

> "Built a multi-agent AI writing system inspired by modern agent architectures, implementing planning, content generation, and refinement pipelines using OpenAI APIs."

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

Inspired by advanced agent-based architectures and modern LLM workflows.

---

⭐ If you like this project, consider giving it a star on GitHub!
