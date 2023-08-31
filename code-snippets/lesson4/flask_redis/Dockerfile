# Use an official Python runtime as a base image
FROM python:3.8-slim AS build

# Set the working directory inside the container
WORKDIR /app

# Use a build argument for environment specification
ARG ENVIRONMENT=production

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Flask and Redis libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory's contents into the container
COPY . .

# Multi-stage build for cleaner final image
FROM python:3.8-slim AS final
WORKDIR /app
COPY --from=build /app /app

# Expose port 5000 for the Flask app to listen on
EXPOSE 50800

# Using both ENTRYPOINT and CMD for flexibility
ENTRYPOINT ["python"]
CMD ["./app.py"]
