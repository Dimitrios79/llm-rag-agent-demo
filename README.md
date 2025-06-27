# 🧠 LLM Medical Agent Demo (Falcon-7B via Hugging Face)

This project is a lightweight proof-of-concept of a medical assistant AI agent using Hugging Face models.

It allows users to ask health-related questions and receive answers generated from an open-source LLM model.

---

## ✅ Features

- 🤖 Uses Falcon-7B-Instruct (tiiuae/falcon-7b-instruct)
- 🔓 100% free with Hugging Face token (no OpenAI cost)
- 🧠 Acts like a helpful medical assistant via prompt engineering
- 💬 Works in CLI or via Web Interface (Gradio)
- 🪶 Easy to modify, extend, and integrate into larger agent systems

---

## 💻 Setup Instructions

### 1. Clone the repo

```
git clone https://github.com/Dimitrios79/llm-rag-agent-demo.git
cd llm-rag-agent-demo
```

### 2. Create virtual environment & install dependencies

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Create `.env` file

Go to [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens), create a read access token, and paste it into `.env`:

```
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxx
```

---

## 🚀 Run the CLI App

```
python app.py
```

You can ask questions like:

```
What are the common types of chronic wounds?
How can I treat pressure ulcers at home?
```

---

## 🌐 Optional: Run with Gradio UI

```
pip install gradio
python app_gradio.py
```

---

## 📎 Model Details

- Model: `tiiuae/falcon-7b-instruct`
- License: Apache 2.0
- Usage: Text generation pipeline (transformers)
- Prompt: "You are a helpful medical assistant. {query}"

---

## 👨‍💻 Author

Dimitrios Kallimanis  
📍 Thessaloniki, Greece  
📧 kallidimi2@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/dimitrioskallimanis/)  
🔗 [GitHub](https://github.com/Dimitrios79)

---

This project was created as part of a technical demo for the WoundHeroes AI agent position.