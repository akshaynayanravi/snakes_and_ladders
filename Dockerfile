# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /snakes_and_ladders

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Copy only dependency files first
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-interaction

# Copy the rest of the application code
COPY . .

# Default command to run (you can customize this as needed)
CMD ["poetry", "run", "python", "main.py"]