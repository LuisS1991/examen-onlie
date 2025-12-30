# Usa la imagen base de Python
FROM python:3.11

# Establece el directorio de trabajo principal
WORKDIR /app

# Copia todo el contenido del proyecto al contenedor
COPY . .

# Variables de entorno para el entorno virtual
ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Crea el entorno virtual
RUN python3.11 -m venv $VIRTUAL_ENV

# Instala las dependencias backend
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Establece el directorio de trabajo a "backend"  /app/backend
WORKDIR /app

# Ejecuta los comandos de migración y luego inicia la app
CMD bash -c "reflex db init && reflex db makemigrations && reflex db migrate && reflex run --env prod --backend-only"
