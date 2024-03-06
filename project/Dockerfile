# Dockerfile

FROM python:3.11

WORKDIR /app

COPY ./app /app

# Установка зависимостей
RUN pip install uvicorn fastapi httpx pytest SQLAlchemy

# Обновление pip
RUN python -m pip install --progress-bar off --upgrade pip

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
