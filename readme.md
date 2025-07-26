# Project Management Application

A full-stack project management application built with React, Flask, and PostgreSQL.

## Tech Stack
- **Frontend:** React 18, Tailwind CSS, Vite
- **Backend:** Flask, SQLAlchemy, PostgreSQL
- **Database:** PostgreSQL
- **Development:** Docker, pytest, ESLint

## Getting Started

### Prerequisites
- Python 3.9+
- Node.js 16+
- PostgreSQL
- Docker (optional)

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your database credentials
flask run