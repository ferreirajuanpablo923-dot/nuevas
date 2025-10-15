FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# Instalar dependencias del proyecto + Selenium
RUN pip install --no-cache-dir -r requirements.txt selenium webdriver-manager

COPY . .

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

CMD ["python", "app.py"]
