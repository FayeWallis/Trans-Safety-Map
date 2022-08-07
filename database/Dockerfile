FROM postgis/postgis

ENV POSTGRES_USER foo
ENV POSTGRES_PASSWORD bar
ENV POSTGRES_DBNAME TSM
ENV ALLOW_IP_RANGE 0.0.0.0/0

RUN psql --host=localhost --username=postgres --file=/run/data/load_data.sql
6