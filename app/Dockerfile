# Imagen base ligera con Python
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar dependencias primero (para aprovechar caché de Docker)
COPY requirements.txt .

# Instalar dependencias sin usar caché
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Definir variables de entorno
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1

# Exponer el puerto donde correrá Flask
EXPOSE 5000

# Comando para ejecutar la app
CMD ["flask", "run"]