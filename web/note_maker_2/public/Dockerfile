FROM python:3.9
WORKDIR /hackentine
COPY ./ ./
RUN pip install -r requirements.txt
RUN useradd freshie_hacker
RUN chown -R root:freshie_hacker /hackentine && chmod -R 750 /hackentine
RUN chmod -R 777 /hackentine/notes
RUN mv ./flag.txt /flag
USER freshie_hacker
ENTRYPOINT ["python3","app.py"]

