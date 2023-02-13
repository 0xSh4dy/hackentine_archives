FROM python:3.11.2-bullseye
WORKDIR /web
COPY ./ ./
RUN pip install -r requirements.txt
RUN useradd n00b
EXPOSE 8002
CMD ["python3","app.py"]