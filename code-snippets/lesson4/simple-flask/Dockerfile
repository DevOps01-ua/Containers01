# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory's contents into the container at /app
COPY . /app

# Install Flask
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask app to listen on
EXPOSE 50800

# Define the command to run the app using python
CMD ["python3", "./simple-flask-application.py"]
