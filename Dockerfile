FROM python:3-alpine
RUN pip install setuptools --upgrade pip
RUN pip install flask --upgrade pip
RUN pip install flask_mysql
COPY . .
ENTRYPOINT APP=app.py flask run
