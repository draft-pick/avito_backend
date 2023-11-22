FROM python:3.9-slim
WORKDIR /app
COPY ./requirements.txt .
RUN pip3 install -r /app/requirements.txt
COPY backend/ /app
CMD ["python3", "manage.py", "runserver", "0:8000"] 