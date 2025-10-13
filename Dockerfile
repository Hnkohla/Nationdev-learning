# Use slim Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Setup database
RUN python manage.py makemigrations core
RUN python manage.py migrate

# Run server
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]