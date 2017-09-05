FROM python:3.5.1

ENV APP_ROOT /usr/src/hinagata-flask

WORKDIR $APP_ROOT

RUN apt-get update && \
    apt-get install -y mysql-client \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt $APP_ROOT

RUN pip install -r requirements.txt

COPY . $APP_ROOT

EXPOSE  5000
CMD ["python", "app.py", "runserver"]