FROM python:3.10-slim

RUN apt-get update && apt-get install -y curl zstd && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://ollama.com/install.sh | sh

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD bash -c "\
ollama serve & \
sleep 10 && \
ollama pull gemma:2b && \
ollama run gemma:2b 'Hello from CI pipeline' && \
echo 'CI test successful' \
"
