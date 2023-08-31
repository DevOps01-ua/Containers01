# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Flask and Redis libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory's contents into the container
COPY . .

# Expose port 5000 for the Flask app to listen on
EXPOSE 5000

# Run the app
CMD ["python", "./app.py"]
