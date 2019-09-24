FROM jfloff/alpine-python:latest

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["pyrhon","manage.py","runserver"]