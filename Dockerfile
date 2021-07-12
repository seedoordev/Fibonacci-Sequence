FROM python:3.9
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./testtask ./testtask

CMD ["python", "./testtask/manage.py", "runserver", "0.0.0.0:8000"]