FROM python:3.9-slim

WORKDIR /app

# Copiar archivos de la app
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto
EXPOSE 5000

CMD ["python", "app.py"]
