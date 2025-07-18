FROM python:3.13.5-slim

WORKDIR /app

RUN apt-get update && apt-get install -y make

RUN pip install --upgrade pip && pip install uv

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV PYTHONPATH="${PYTHONPATH}:/app/src"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . /app

RUN uv install
