# Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /app

# dependencias del sistema para psycopg2 u otras libs
RUN apt-get update && apt-get install -y build-essential libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Copia solo lo necesario para caché de pip
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia el resto del código
COPY . /app

# Collect static si lo necesitas (descomenta si usas)
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "ToDoApp.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120"]

