FROM python:3.9
WORKDIR /app
RUN apt-get update && apt-get install -y socat
RUN useradd n00b
COPY ./script.py ./
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
RUN chown -R root:n00b /app/ && chmod -R 750 /app/
USER n00b
CMD ["socat","TCP-LISTEN:8034,fork","EXEC:/usr/local/bin/python /app/script.py"]

