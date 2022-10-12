FROM python:3.9-alpine


ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

#  dependencies for psycopg2 
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt .dockerignore ./

# modify permissions for the entrypoint.sh before running the docker build
COPY entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]