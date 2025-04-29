# Usar la última versión de Python
FROM python:3.12

# Definir el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de requerimientos e instalarlos
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del proyecto
COPY . .

# Exponer el puerto para el servidor de desarrollo
EXPOSE 8000

# Comando por defecto al iniciar el contenedor
# CMD ["sleep", "infinity"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

