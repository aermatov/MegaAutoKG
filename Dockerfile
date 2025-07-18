FROM python:3.12-slim

WORKDIR /app

# Установка зависимостей (в одной RUN инструкции)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Создаем пользователя для Celery
RUN groupadd -r celery && useradd -r -g celery celery

# Установка Python зависимостей
RUN pip install --upgrade pip && pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY . .

# Устанавливаем права
RUN chown -R celery:celery /app

CMD ["bash", "entrypoint.sh"]