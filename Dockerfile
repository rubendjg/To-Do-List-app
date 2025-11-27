FROM python:3.11-slim

ARG SECRET_KEY
ENV SECRET_KEY=${SECRET_KEY}

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update && apt-get install -y build-essential libpq-dev gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "ToDoApp.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120"]

