FROM python:3.9

WORKDIR /app
COPY Requirenment.txt /app

RUN pip install -r Requirenment.txt

CMD ["python", "app.py", "dev"]

