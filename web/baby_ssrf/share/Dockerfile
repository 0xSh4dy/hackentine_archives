FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./run.sh .
RUN chmod +x run.sh
COPY app1 /app/app1
COPY app2 /app/app2
EXPOSE 8010
EXPOSE 8100
CMD ["./run.sh"]
