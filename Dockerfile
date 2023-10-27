FROM python:3.11.4-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt 

COPY ./ .

# CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
CMD gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000