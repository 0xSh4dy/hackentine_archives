FROM python:3.9
RUN apt-get update && apt-get install -y socat
WORKDIR /app
COPY pyjail2.py ./pyjail2.py
COPY flag.txt ./flag.txt
RUN useradd n00b
RUN chown -R root:n00b /app && chmod -R 750 /app
USER n00b
CMD ["socat","TCP-LISTEN:8033,fork","EXEC:/usr/local/bin/python /app/pyjail2.py"]