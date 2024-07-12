FROM python:alpine3.20

WORKDIR /app

COPY . . 

RUN python -m pip install --upgrade pip
RUN pip install -r requirement.txt

CMD ["python", "app.py"]

