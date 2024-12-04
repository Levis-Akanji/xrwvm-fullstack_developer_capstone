# Base image
FROM python:3.12.0-slim-bookworm

# Environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONWRITEBYTECODE 1
ENV APP=/app

# Change working directory
WORKDIR $APP

# Copy and install dependencies
COPY requirements.txt $APP/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy application files
COPY . $APP

# Expose application port
EXPOSE 8000

# Set entrypoint and command
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]
