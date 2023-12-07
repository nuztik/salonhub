FROM python:3.11.7


WORKDIR /usr/src/app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PETHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver"]
