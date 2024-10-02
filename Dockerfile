FROM python:3.7

WORKDIR /app
COPY Requirenment.txt /app

RUN pip install -r Requirenment.txt

CMD ["python", "app.py", "dev"]

