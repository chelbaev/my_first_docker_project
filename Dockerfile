FROM python:alpine

WORKDIR /application

COPY requirements.txt /application

RUN pip install -r requirements.txt 

COPY . /application

CMD ["python", "table.py"]