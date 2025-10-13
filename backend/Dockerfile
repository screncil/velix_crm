# 1. Базовый образ Python
FROM python:3.12-slim

# 2. Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# 4. Устанавливаем зависимости системы (для psycopg2, Pillow и т.д.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gettext \
    && rm -rf /var/lib/apt/lists/*

# 5. Копируем зависимости проекта
COPY requirements.txt .

# 6. Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# 7. Копируем весь код Django внутрь контейнера
COPY . .

# 8. Открываем порт
EXPOSE 8000

# 9. Команда по умолчанию — запуск сервера разработки
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
