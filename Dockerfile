FROM python:3.12-slim-bookworm

# Set work directory
WORKDIR /app

# Copy requirements.txt from the app directory
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire app folder into the container
COPY app/ ./

# Expose the port the app runs on
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]