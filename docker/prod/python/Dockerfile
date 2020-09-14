FROM python:3.8
# MAINTAINER tito@localhost

WORKDIR /app

COPY ./app/requirements /app/requirements

RUN pip install --no-cache-dir -r requirements/requirements.txt

COPY ./app /app
RUN export PYTHONPATH=`pwd`

WORKDIR /app/src


# EXPOSE 8000


# COPY ./docker/prod/python/entrypoint.sh /entrypoint.sh
# RUN chmod +x /entrypoint.sh

# ENTRYPOINT ["/entrypoint.sh"]

# CMD ["gunicorn", "woozy.wsgi", "-b 0.0.0.0:8000"]