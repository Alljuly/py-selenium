FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    libx11-dev \
    libdbus-glib-1-2 \
    libxt6 \
    libgtk-3-0 \
    libasound2 \
    libdbus-1-3 \
    xdg-utils \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.36.0/geckodriver-v0.36.0-linux64.tar.gz && \
    tar -xvzf geckodriver-v0.36.0-linux64.tar.gz && \
    mv geckodriver /usr/local/bin/ && \
    rm geckodriver-v0.36.0-linux64.tar.gz

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app", "--timeout", "120"]
