FROM python:3.8.2-alpine3.11
COPY . .
RUN pip3 install -r requirements.txt
CMD python3 manage.py runserver 0.0.0.0:8080
EXPOSE 8080 
