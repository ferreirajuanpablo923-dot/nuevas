# =========================
#  Dockerfile para validator
# =========================
FROM python:3.11-slim

WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
