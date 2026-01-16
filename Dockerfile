FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for tree-sitter
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    vim \
    less \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY parsers/ ./parsers/
COPY generators/ ./generators/
COPY doc_generator.py .

# Make the script executable
RUN chmod +x doc_generator.py

# Create symlink so doc_generator.py is available in PATH
RUN ln -s /app/doc_generator.py /usr/local/bin/doc_generator.py

# Create a wrapper script that allows exec access
RUN echo '#!/bin/bash\n\
if [ "$1" = "service" ]; then\n\
    echo "================================================"\n\
    echo "Documentation Generator Service is running..."\n\
    echo "================================================"\n\
    echo ""\n\
    echo "Available commands:"\n\
    echo "  docker exec -it <container> doc_generator.py <path> [--output FILE]"\n\
    echo "  docker exec -it <container> bash"\n\
    echo "  docker exec -it <container> ls -la /workspace"\n\
    echo ""\n\
    echo "Current workspace: /workspace"\n\
    echo "================================================"\n\
    tail -f /dev/null\n\
else\n\
    exec python /app/doc_generator.py "$@"\n\
fi' > /usr/local/bin/entrypoint.sh && \
    chmod +x /usr/local/bin/entrypoint.sh

# Set the entry point
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# Default: run as service (keeps container alive for exec)
CMD ["service"]
