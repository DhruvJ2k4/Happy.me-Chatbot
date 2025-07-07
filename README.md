# Happy.me-Chatbot

[![CI](https://img.shields.io/github/actions/workflow/status/DhruvJ2k4/Happy.me-Chatbot/ci.yml?branch=master)](https://github.com/DhruvJ2k4/Happy.me-Chatbot/actions)
[![Coverage](https://img.shields.io/badge/coverage-unknown-lightgrey)](https://github.com/DhruvJ2k4/Happy.me-Chatbot/actions)
[![Version](https://img.shields.io/github/v/release/DhruvJ2k4/Happy.me-Chatbot)](https://github.com/DhruvJ2k4/Happy.me-Chatbot/releases)
[![License](https://img.shields.io/github/license/DhruvJ2k4/Happy.me-Chatbot)](https://github.com/DhruvJ2k4/Happy.me-Chatbot/blob/master/LICENSE)

---

## Overview

**Happy.me-Chatbot** is a real-time web application that uses webcam-based facial emotion recognition to detect user mood and provide responsive, empathetic chatbot interactions. Leveraging modern web technologies, a robust Python backend, and GPT-powered language understanding, Happy.me-Chatbot strives to create a supportive environment, enhance user well-being, and offer seamless multilingual support.

### Value Proposition

- **Empathetic, Real-Time Conversations** via emotion-aware AI
- **Privacy-Respecting** facial analysis performed locally/in-browser
- **Multilingual**: Breaks language barriers
- **Exportable Chat History**: Download your conversations as PDF/Word
- **Developer-Friendly**: Modular, extensible, CI/CD ready

---

## Architecture

- **Frontend**: TypeScript, Next.js, Tailwind CSS
- **Backend**: Python (FastAPI), emotion recognition, GPT integration
- **GPT Integration**: Uses OpenAI/Gemini for context-aware chatbot responses
- **State Management**: Modern React hooks
- **Facial Recognition**: WebRTC/Webcam to backend ML pipeline

```
Frontend (Next.js/React) <--> FastAPI backend <--> GPT/ML services
                      ^           ^
                Webcam & UI    Auth/DB/Export
```

---

## Installation

### Prerequisites

- Python 3.9+
- Node.js 18+/Yarn
- [Virtualenv](https://virtualenv.pypa.io/) (Recommended)

### Setup

```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate on Windows
pip install -r requirements.txt

# Frontend
cd ../frontend
yarn install
```

---

## Usage

### Launch locally

```bash
# Start backend (by default on http://localhost:8000)
cd backend
uvicorn app.main:app --reload

# Start frontend (by default on http://localhost:3000)
cd ../frontend
yarn dev
```

### Streamlit Launch (if available)

```bash
cd backend
streamlit run app/streamlit_app.py
```
> The Streamlit app provides a research/demo dashboard for live emotion detection and chat.

---

### Multilingual Support

- Automatic language detection and translation
- UI and chatbot support for English, Hindi, Spanish, French, and more.

---

## Features

- **Webcam-based Emotion Recognition**: Real-time facial analysis
- **Empathetic GPT Chatbot**: Adapts tone and responses
- **Multilingual Conversations**
- **History Export**: Download chat as PDF/Word (`Export` button in UI)
- **User Authentication**: Secure, JWT-based
- **Mobile-Optimized UI**
- **Accessible Design**

---

## Exporting Chat History

- After a chat session, use the "Export" button to download your conversation as a PDF or Word document.
- Export logic is handled in the backend and frontend integration.

---

## Supported Languages

- English, Hindi, Spanish, French, more (contributions welcome!)

---

## Development Guidelines

- **Branch Strategy**: Use `main` for production, `dev` for integration, feature branches for new work.
- **Linting**: 
  - Frontend: `yarn lint`
  - Backend: `flake8`, `black`
- **Testing**: 
  - Frontend: `yarn test`
  - Backend: `pytest`
- **CI/CD**: GitHub Actions for linting, testing and deployment.
- **Commits**: Follow [Conventional Commits](https://www.conventionalcommits.org/).
- **Changelog**: See [CHANGELOG.md](https://github.com/DhruvJ2k4/Happy.me-Chatbot/blob/master/CHANGELOG.md) (if available).

---

## Contribution

We welcome contributions! Please follow the [CONTRIBUTING.md](CONTRIBUTING.md) guidelines.

- Open an issue for discussion before large changes.
- All PRs require review.
- Add/Update tests for new features.

---

## Deployment

### Docker

You can deploy both backend and frontend using Docker.

```bash
# Example Docker Compose (not exhaustive)
docker-compose up --build
```
> See `docker-compose.yml` if available, or create Dockerfiles for backend/frontend.

### Cloud

- Deployable on major cloud platforms (AWS, GCP, Azure).
- Environment variables for secrets and configuration.

---

## Environment Variables

- **Backend**: `.env` for DB, secret keys, GPT/OpenAI credentials, etc.
- **Frontend**: `.env.local` for API endpoints, public keys.

| Variable                | Description                          |
|-------------------------|--------------------------------------|
| OPENAI_API_KEY          | OpenAI GPT API Key                   |
| GEMINI_API_KEY          | Google Gemini API Key                |
| DATABASE_URL            | Database connection string           |
| SECRET_KEY              | JWT/Session secret                   |
| FRONTEND_URL            | URL to frontend app                  |
| ...                     | See `.env.example` for all           |

---

## License

This project is licensed under the [MIT License](https://github.com/DhruvJ2k4/Happy.me-Chatbot/blob/master/LICENSE).

---

## Authors

- [DhruvJ2k4](https://github.com/DhruvJ2k4), and contributors.

---

## Changelog

See [CHANGELOG.md](https://github.com/DhruvJ2k4/Happy.me-Chatbot/blob/master/CHANGELOG.md) for release history.

---

> _Note: Some file/discovery results above may be incomplete due to code search/API limits. For more details, browse the [repo on GitHub](https://github.com/DhruvJ2k4/Happy.me-Chatbot)._
