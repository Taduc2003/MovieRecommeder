FROM python:3.8-slim

WORKDIR /app

# Cài đặt gcc, g++, và các thư viện cần thiết để build C-extension
RUN apt-get update && \
    apt-get install -y gcc g++ python3-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt && pip install scikit-surprise --no-build-isolation


COPY ./src /app

ENV PYTHONUNBUFFERED=1

CMD ["gunicorn", "cfehome.wsgi:application", "--bind", "0.0.0.0:8000"]