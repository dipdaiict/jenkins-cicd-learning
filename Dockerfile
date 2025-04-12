# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy app code to container
COPY app.py .

# Install dependencies
RUN pip install fastapi uvicorn

# Expose port
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
