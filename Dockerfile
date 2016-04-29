FROM python:onbuild

CMD ["gunicorn",
     "--user", "www-data",
     "--worker-class", "gevent",
     "--access-logfile", "-", "--error-logfile", "-",
     "-b", "0.0.0.0:8000",
     "sunsurfers.wsgi:application"]
