# 🎮 To-Do List App - Retro Pixel Art Edition

A modern Django-based task management application with a retro 8-bit gaming aesthetic — now fully containerized with Docker, PostgreSQL, Prometheus, and Grafana.

---

## ✨ Features

- Retro 8‑bit pixel UI
- User signup/login/logout
- Full task CRUD
- Deadlines & completion tracking
- Responsive UI with Bootstrap
- PostgreSQL support (via Docker)
- Prometheus metrics
- Grafana dashboards

---

# 🚀 Quick Start (Local or Docker)

## Prerequisites

- Docker + Docker Compose
- (Optional) Python 3.11+

---

# ▶️ Running with Docker

## 1. Create `.env`

```
SECRET_KEY=localdevsecret123
DEBUG=True
DATABASE_URL=postgres://postgres:postgres@db:5432/todo_db
ENVIRONMENT=dev
```



Before building the Docker container, run this command to make sure the system identifies the ENV\_FILE

Windows PowerShell:

```
$env:ENV_FILE=".env"
```

Linux/macOS:

```
export ENV_FILE=.env
```

## 2. Build & run

```
docker compose up --build
```

### Services

- **Web**: [http://localhost:8000](http://localhost:8000)
- **Prometheus**: [http://localhost:9090](http://localhost:9090)
- **Grafana**: [http://localhost:3000](http://localhost:3000) (admin/admin)

## 3. Stop

```
docker compose down
```

---

# ▶️ Running Locally (Without Docker)

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

# 🧪 Testing

```
python manage.py test
python manage.py makemigrations --check
flake8 .   # optional
```

---

# 🚀 Deployment Guide

## Build production image

```
docker build -t todoapp-prod .
```

## Production environment

```
SECRET_KEY=randomstring
DEBUG=False
DATABASE_URL=postgres://user:pass@host:5432/dbname
```

## Run stack

```
docker compose up -d
```

Gunicorn automatically serves the app. Prometheus & Grafana start automatically.

---

# 📁 Project Structure

```
To-Do app/
├── manage.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── prometheus.yml
├── tasks_app/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── static/
│   ├── templates/
│   └── migrations/
└── ToDoApp/
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

---

# 🎨 Design

- Pixel fonts: Orbitron, VT323
- Gold + Forest green palette
- Pixel icons (edit, delete, complete, login, etc.) created in Aseprite

---

# 🔧 Technical Details

- Django 5.2.6
- Python 3.11+
- PostgreSQL via Docker
- Bootstrap 5.3.2
- Prometheus + Grafana

---

# 🤝 Contributing

```
git checkout -b feature/YourFeature
commit & push
open PR
```

---

# 📝 License

MIT License

---

# 📞 Contact

**Developer**: Ruben DJG GitHub: [https://github.com/rubendjg/To-Do-List-app](https://github.com/rubendjg/To-Do-List-app)

