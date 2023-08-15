# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory in container
COPY . /app
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source files
COPY . .

# Command to run the app (modify as per your app's start command)
CMD ["python", "src/app.py"]
