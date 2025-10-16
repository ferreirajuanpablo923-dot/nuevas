# =========================
#  Dockerfile para Flask App
# =========================
FROM python:3.11-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de dependencias
COPY requirements.txt .

# Instalar dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el contenido del proyecto al contenedor
COPY . .

# Exponer el puerto por el que correrá Flask
EXPOSE 5000

# Variables de entorno
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=8.0.8.0
ENV FLASK_ENV=production

# Comando para iniciar la app Flask
CMD ["python", "app.py"]
