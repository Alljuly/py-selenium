FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    ca-certificates \
    libgtk-3-0 \
    libdbus-glib-1-2 \
    libxt6 \
    libx11-6 \
    libxcomposite1 \
    libxrandr2 \
    libasound2 \
    libnss3 \
    libgdk-pixbuf2.0-0 \
    libatspi2.0-0 \
    libgconf-2-4 \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y firefox-esr

RUN curl -sSL https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz | tar xz -C /usr/local/bin

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app", "--timeout", "120"]
