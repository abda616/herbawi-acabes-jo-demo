# Python Redis — Dockerized App with CI

This repository contains a minimal Python application that interacts with a Redis instance. It reads a key from Redis, sets a default value if the key does not exist, and prints the result. The app is containerized with Docker and includes a GitHub Actions workflow to build and publish the image as an artifact.

## Repository layout

- src/main.py — entry point for the Python app.
- src/requirements.txt — Python dependencies.
- container/Dockerfile — image definition for building a container.
- .github/workflows/container-build.yaml — CI workflow that builds and uploads a Docker image artifact on pushes to main.

## Prerequisites

- Python 3.11+ (only for running locally without Docker)
- Docker (for container builds and runs)
- A running Redis instance (local or remote)

## Running locally (without Docker)

1. Start a Redis instance (example using Docker):
   ```
   docker run -d --name redis -p 6379:6379 redis:7
   ```
2. Install dependencies:
   ```
   pip install -r src/requirements.txt
   ```
3. Run the app:
   ```
   ENV_VAR_REDIS=localhost \
   ENV_VAR_RPORT=6379 \
   ENV_VAR_RKEY=hello \
   ENV_VAR_RVALUE="World!" \
   python src/main.py
   ```

## Configuration

The application uses the following environment variables:

- ENV_VAR_REDIS — Redis host (default: localhost)
- ENV_VAR_RPORT — Redis port (default: 6379)
- ENV_VAR_RKEY — Redis key to read/write (default: hello)
- ENV_VAR_RVALUE — Default value to set if key is missing (default: world!/World! in Docker image)

You can override these when running locally or in Docker (see examples below).

## Docker

### Build the image

Run from the repository root:
``` 
docker build -f .\container\Dockerfile  -t herbawi-acabes-jo-demo .
```
  
### Run the container
``` 
docker run --name herbawi-acabes-jo-demo --env=ENV_VAR_REDIS=192.168.100.7 --env=ENV_VAR_RKEY='welocome' --env=ENV_VAR_RVALUE='to Docker' --env=ENV_VAR_RPORT=6379 -d herbawi-acabes-jo-demo:latest 
```

### To stop (kill) the container:
```
docker stop herbawi-acabes-jo-demo
```

### To remove the container:
```
docker rm herbawi-acabes-jo-demo
```


