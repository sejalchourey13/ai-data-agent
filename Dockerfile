FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    zstd \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Ollama port
EXPOSE 11434

# Start Ollama, pull model, then run agent
CMD ["sh", "-c", "ollama serve & sleep 5 && ollama pull gemma:2b && python agent/main.py"]
