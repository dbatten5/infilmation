FROM python:3.9.2-slim-buster

ENV WORKDIR=/usr/src/app
ENV USER=app
ENV APP_HOME=/home/app/web
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR $WORKDIR

RUN pip install --upgrade pip
COPY ./app/requirements.txt $WORKDIR/requirements.txt
RUN pip install -r requirements.txt

RUN adduser --system --group $USER
RUN mkdir $APP_HOME

COPY ./app $APP_HOME
RUN chown -R $USER:$USER $APP_HOME
USER $USER
