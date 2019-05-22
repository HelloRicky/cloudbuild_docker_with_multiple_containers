FROM python:3.6.5-stretch
COPY . /
RUN pip3 install psycopg2
CMD ["/bin/bash", "docker-entrypoint.sh"]
