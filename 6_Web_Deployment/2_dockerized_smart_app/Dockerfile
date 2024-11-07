FROM python:3.9-slim

#just edited
WORKDIR /app

#just edited
COPY . /app


RUN pip install --no-cache-dir -r requirements.txt

#just added
ENV FLASK_APP=app.py

EXPOSE 5000

#CMD [ "python", "app.py" ]
# using following command instead former. 
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
