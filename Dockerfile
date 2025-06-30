FROM python:3.10
 
WORKDIR /app
COPY . /app
 
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev gcc && \
    pip install -r requirements.txt
 
CMD ["python", "app.py"]
