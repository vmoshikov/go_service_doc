# Docker Usage Guide

## Quick Start

### Build the Image

```bash
docker build -t go-doc-generator .
```

### Run as Service (Recommended)

Start the service container (stays running for exec access):

```bash
docker run -d --name doc-gen \
  -v /path/to/your/go-service:/workspace \
  go-doc-generator
```

### Execute Commands

Once the container is running, you can execute commands:

```bash
# Generate documentation
docker exec -it doc-gen doc_generator.py /workspace

# Generate with custom output file
docker exec -it doc-gen doc_generator.py /workspace --output CUSTOM_README.md

# Access interactive shell
docker exec -it doc-gen bash

# List files in workspace
docker exec -it doc-gen ls -la /workspace

# View generated docs
docker exec -it doc-gen ls -la /workspace/docs

# Check if Go service exists
docker exec -it doc-gen test -d /workspace && echo "Directory exists"
```

### View Container Logs

```bash
docker logs doc-gen
```

### Stop and Remove

```bash
docker stop doc-gen
docker rm doc-gen
```

## Using Docker Compose

### Start Service

```bash
docker-compose up -d
```

### Execute Generator

```bash
docker-compose exec doc-generator doc_generator.py /workspace
```

### Access Shell

```bash
docker-compose exec doc-generator bash
```

### Stop Service

```bash
docker-compose down
```

## Mount Multiple Paths

You can mount multiple directories:

```bash
docker run -d --name doc-gen \
  -v /path/to/go-service-1:/workspace/service1 \
  -v /path/to/go-service-2:/workspace/service2 \
  go-doc-generator

# Generate docs for service 1
docker exec -it doc-gen doc_generator.py /workspace/service1

# Generate docs for service 2
docker exec -it doc-gen doc_generator.py /workspace/service2
```

## Troubleshooting

### Check if container is running

```bash
docker ps | grep doc-gen
```

### View container status

```bash
docker inspect doc-gen
```

### Access container even if it's stopped

```bash
docker start doc-gen
docker exec -it doc-gen bash
```

### Rebuild after code changes

```bash
docker build -t go-doc-generator .
docker stop doc-gen && docker rm doc-gen
docker run -d --name doc-gen -v /path/to/go-service:/workspace go-doc-generator
```
