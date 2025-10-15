FROM python:3.11-slim

# Dependencias necesarias para Chrome
RUN apt-get update && apt-get install -y \
    wget unzip gnupg2 fonts-liberation libnss3 libx11-xcb1 libxcomposite1 libxcursor1 \
    libxdamage1 libxi6 libxtst6 libxrandr2 libasound2 libpangocairo-1.0-0 libatk-bridge2.0-0 \
    libgtk-3-0 libcups2 libdbus-1-3 libxss1 libxshmfence1 xdg-utils --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Instalar Google Chrome
RUN wget -qO google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -y ./google-chrome.deb \
    && rm google-chrome.deb

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt selenium webdriver-manager

COPY . .

EXPOSE 5000
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

CMD ["python", "app.py"]
