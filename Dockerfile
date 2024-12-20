# Build stage: Install dependencies
FROM python:3.10-slim as builder

# Set the working directory
WORKDIR /app

# Copy pyproject.toml and poetry.lock
COPY pyproject.toml poetry.lock ./

# Install Poetry
RUN pip install poetry

# Use Poetry to install dependencies to a temporary directory
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Runtime stage: Copy necessary files and start the application
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy dependencies installed in the build stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy project code
COPY confluence2markdown confluence2markdown

# Expose the port
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "confluence2markdown.rest_api.main:app", "--host", "0.0.0.0", "--port", "8000"]