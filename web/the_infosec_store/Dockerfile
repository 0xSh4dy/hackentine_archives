FROM python:3.9
WORKDIR /hackentine
COPY ./ ./
RUN pip install -r requirements.txt
RUN useradd freshie_hacker
RUN chown -R root:freshie_hacker /hackentine && chmod -R 750 /hackentine
RUN chmod 777 /hackentine/db.json
USER freshie_hacker
EXPOSE 8013
ENTRYPOINT ["python3","app.py"]

