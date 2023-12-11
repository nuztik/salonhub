FROM python:3.11.7-slim-bookworm AS venv

#задаем значения переменных
ENV PYTHONDONTWRITEBYTECODE 1
ENV PETHONUNBUFFERED 1

#обновление pip
RUN pip install --upgrade pip

#установка пакетов для проекта
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#задаем рабочую директорию контейнера
WORKDIR /usr/src/app

# Копирование проекта
COPY . .

# Настройка записи и доступа
RUN chmod -R 777 ./
