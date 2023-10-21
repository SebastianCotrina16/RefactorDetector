FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

COPY action/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY scripts/ /app/scripts/
COPY action/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
