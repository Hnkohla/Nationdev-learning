# Use slim Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
ENV DJANGO_SETTINGS_MODULE nationdev.settings

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Setup database
RUN python manage.py makemigrations core
RUN python manage.py migrate

# Run gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "nationdev.wsgi:application"]

# Expose port
EXPOSE 8000

# Run server
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]