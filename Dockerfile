FROM mcr.microsoft.com/playwright/python:v1.60.0-noble

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

RUN playwright install --with-deps

COPY . .
CMD ["pytest"]