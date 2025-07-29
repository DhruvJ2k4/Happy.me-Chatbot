# 😊 Happy.me – Emotion-Aware Conversational Chatbot

> Real-time facial emotion recognition meets empathetic AI conversations.

---

## 🚀 Overview

**Happy.me** is a full-stack AI chatbot that leverages real-time webcam-based emotion detection and conversational intelligence to deliver empathetic, and context-aware experiences. The chatbot dynamically adjusts its responses based on the user’s detected emotions and provides features such as secure authentication and exportable chat history.

---

## 🧠 Features

- 🎥 Real-time facial emotion recognition via webcam
- 💬 Emotion-aware Gemini conversational AI
- 📤 Chat export as PDF and Word
- 🔐 Secure JWT-based authentication
- 📱 Responsive UI built with modern React stack

---

## 🏗️ Tech Stack

| Layer                  | Stack                                    |
|------------------------|------------------------------------------|
| Frontend               | Next.js, TypeScript, Tailwind CSS        |
| Backend                | FastAPI (Python), SQLite/PostgreSQL      |
| Chatbot Model          | Gemini API, NLTK, Spacy                  |
| Computer Vision Model  | CNN-based emotion detection using PyTorch|
| Export                 | ReportLab, python-docx for file export   |

---

## 📁 Project Structure

```
Happy.me-Chatbot/
├── backend/
│   └── app/
│       ├── main.py
│       ├── emotion/
│       ├── chatbot/
│       ├── export/
│       ├── auth/
│       └── models/
└── frontend/
    ├── pages/
    ├── components/
    ├── hooks/
    └── public/
```

## ⚙️ Installation

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Frontend

```bash
cd frontend
yarn install
```

---

## 🧪 Running Locally

### Backend (FastAPI)

```bash
cd backend
uvicorn app.main:app --reload
```

### Frontend (Next.js)

```bash
cd frontend
yarn dev
```


---

## 🔐 Environment Variables

### Backend `.env`
```
OPENAI_API_KEY=your_api_key
SECRET_KEY=your_secret
DATABASE_URL=sqlite:///./test.db
ALLOWED_ORIGINS=http://localhost:3000
```

### Frontend `.env.local`
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 💬 Emotion-Aware AI Chatbot

- Emotion is detected from the user’s webcam stream
- Chat prompts are generated with emotional context
- Supports Google’s Gemini as backend

## 🐳 Docker Support

### Example Docker Compose Setup

```yaml
version: "3"
services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    env_file:
      - ./backend/.env

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    env_file:
      - ./frontend/.env.local
```

## 🛣️ Roadmap

- [ ] Text-to-speech audio replies
- [ ] Emotion trend visualization
---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes with conventional commit messages
4. Push the branch and create a pull request

---

## 📝 License

MIT License © 2024

## ✍️ Authors
[Dhruv Kalpesh Jadav](https://github.com/DhruvJ2k4)
