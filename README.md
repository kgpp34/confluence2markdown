# Confluence2Markdown

Confluence2Markdown is a tool to convert Confluence documents to Markdown format. It provides a REST API for converting Confluence pages to Markdown and a command-line interface for batch conversion.

---

## Features

- **REST API**: Convert Confluence pages to Markdown via API.
- **CLI Tool**: Batch convert Confluence pages to Markdown files.
- **Docker Support**: Easily deploy the application using Docker.
- **Kubernetes Support**: Deploy the application on Kubernetes with a single command.

---

## Installation

### 1. Local Installation

#### Prerequisites

- Python 3.10 or higher
- Poetry (for dependency management)

#### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/confluence2markdown.git
   cd confluence2markdown
   ```
2. Install dependencies:
   ```bash
   poetry install
   ```
3. Set environment variables:
   ```bash
   export CONFLUENCE_BASE_URL=https://your-confluence-instance.com
   export CONFLUENCE_USERNAME=your-username
   export CONFLUENCE_PASSWORD=your-api-key
   export HOST=0.0.0.0
   export PORT=8080
   ```
4. Start the application:
   ```bash
   poetry run uvicorn confluence2markdown.rest_api.main:app --host $HOST --port $PORT
   ```

### 2. Docker Deployment

#### Prerequisites

- Docker installed on your machine.

#### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/confluence2markdown.git
   cd confluence2markdown
   ```
2. Build the Docker image:
   ```bash
   docker build -t confluence2markdown .
   ```
3. Set environment variables:
   ```bash
   export CONFLUENCE_BASE_URL=https://your-confluence-instance.com
   export CONFLUENCE_USERNAME=your-username
   export CONFLUENCE_PASSWORD=your-api-key
   export HOST=0.0.0.0
   export PORT=8080
   ```
4. Run the Docker container:
   ```bash
   docker run -p 8080:8080 \
     -e CONFLUENCE_BASE_URL=$CONFLUENCE_BASE_URL \
     -e CONFLUENCE_USERNAME=$CONFLUENCE_USERNAME \
     -e CONFLUENCE_PASSWORD=CONFLUENCE_PASSWORD \
     -e HOST=$HOST \
     -e PORT=$PORT \
     confluence2markdown
   ```
   

## API Usage

### 1. Convert a Confluence Page by Page ID

```bash
GET /api/page/{page_id}
```

**Example**
```bash
GET http://127.0.0.1:8000/api/page/12345
```

**Response**
```json
{
  "page_id": "12345",
  "markdown": "# Hello, World!\n\nThis is a test."
}
```

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! 


