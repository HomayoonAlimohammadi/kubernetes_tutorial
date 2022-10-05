FROM python:3.8

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./test_project .
EXPOSE 8000

CMD ["python", "manage.py", "runserver"]