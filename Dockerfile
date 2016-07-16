FROM ubuntu

RUN apt update \
 && apt upgrade -y \
 && apt install -y \
    python3 \
    python3-dev \
    python3-pip \
    libgeos-dev \
    libpq-dev \
    libxml2-dev libxslt-dev \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /usr/src/app/
RUN pip3 install -r /usr/src/app/requirements.txt

COPY . /usr/src/app

CMD ["gunicorn", "--user", "www-data", "--worker-class", "gevent", "--access-logfile", "-", "--error-logfile", "-", "-b", "0.0.0.0:8000", "sunsurfers.wsgi:application"]
