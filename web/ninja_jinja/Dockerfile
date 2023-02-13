FROM python:3.11.2-bullseye
WORKDIR /web
COPY ./ ./
RUN pip install -r requirements.txt
RUN useradd n00b
RUN chown -R root:n00b /web && chmod -R 750 /web
EXPOSE 8002
USER n00b
CMD ["python3","app.py"]