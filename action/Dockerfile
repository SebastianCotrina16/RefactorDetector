FROM python:3.11

WORKDIR /action

COPY ./scripts/analyze.py /action/
COPY ./action/requirements.txt /action/
COPY ./action/entrypoint.sh /action/

RUN pip install -r requirements.txt

ENTRYPOINT ["/action/entrypoint.sh"]
