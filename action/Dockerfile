FROM python:3.11-slim

WORKDIR /app

COPY action/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY scripts/ /app/scripts/

COPY action/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
