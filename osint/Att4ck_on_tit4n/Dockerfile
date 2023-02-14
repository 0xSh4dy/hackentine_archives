FROM python:3.9
WORKDIR /app
RUN apt-get update && apt-get install -y socat
RUN useradd n00b
COPY ./source.py ./
RUN chown -R root:n00b /app/ && chmod -R 750 /app/
USER n00b
CMD ["socat","TCP-LISTEN:8035,fork","EXEC:/usr/local/bin/python /app/source.py"]

