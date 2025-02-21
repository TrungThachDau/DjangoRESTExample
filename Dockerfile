FROM python:3.13-slim

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Bundle app source
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Add a health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/ || exit 1

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000","--noreload"]