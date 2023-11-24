FROM python:3.9-slim
WORKDIR /app
COPY ./requirements.txt .
RUN pip3 install -r /app/requirements.txt
COPY . .
CMD ["python3", "/app/manage.py", "runserver", "0.0.0.0:8000"] 