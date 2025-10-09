# Backend Dockerfile (Django)
FROM python:3.12-slim

# Настройки окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y libpq-dev gcc

# Рабочая директория
WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем код
COPY . .

# Команда запуска (для dev)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
