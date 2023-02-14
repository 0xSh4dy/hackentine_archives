FROM python:3.9

RUN apt-get update && apt-get install -y socat

WORKDIR /app

COPY jail1.py ./jail1.py
COPY flag.txt ./flag.txt
RUN useradd n00b
RUN chown -R root:n00b /app/ && chmod -R 750 /app
USER n00b
CMD ["socat", "TCP-LISTEN:8032,fork", "EXEC:/usr/local/bin/python /app/jail1.py"]
EXPOSE 8032