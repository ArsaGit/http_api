FROM python:3.9-slim

# ENV PG_CONFIG=pg_remote

WORKDIR /app

COPY . /app

EXPOSE 5001

RUN pip install -r requirements.txt

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5001", "run:app"]