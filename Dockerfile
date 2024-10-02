FROM python:2.2.3

WORKDIR /app
COPY Requirenment.txt /app

RUN pip install -r Requirenment.txt

CMD ["python", "app.py", "dev"]

