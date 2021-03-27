FROM python:3.9.2-alpine

ENV WORKDIR=/app
ENV USER=app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR $WORKDIR

RUN apk add --update --no-cache g++ gcc libxslt-dev musl-dev postgresql-dev

RUN pip install --upgrade pip
COPY ./app/requirements.txt $WORKDIR/requirements.txt
RUN pip install -r requirements.txt

COPY ./app $WORKDIR
ENV PYTHONPATH=$WORKDIR
