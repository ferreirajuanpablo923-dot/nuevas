# Imagen base ligera de Python
FROM python:3.11-slim

# Variables para que Chrome Headless funcione bien
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependencias mínimas necesarias para Chrome y Selenium
RUN apt-get update && apt-get install -y \
    wget unzip gnupg2 fonts-liberation libnss3 libx11-xcb1 libxcomposite1 \
    libxcursor1 libxdamage1 libxi6 libxtst6 libxrandr2 libasound2 \
    libpangocairo-1.0-0 libatk-bridge2.0-0 libgtk-3-0 libcups2 libdbus-1-3 \
    libxss1 libxshmfence1 xdg-utils --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Instalar Google Chrome estable en modo headless
RUN wget -qO /tmp/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -y /tmp/chrome.deb \
    && rm /tmp/chrome.deb

# Directorio de trabajo
WORKDIR /app

# Copiar e instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt selenium webdriver-manager

# Copiar la aplicación
COPY . .

# Exponer el puerto de Flask
EXPOSE 5000

# Variables de entorno para Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Comando para iniciar la app
CMD ["python", "app.py"]
