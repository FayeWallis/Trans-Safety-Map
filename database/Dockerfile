FROM postgis/postgis

ENV POSTGRES_USER foo
ENV POSTGRES_PASSWORD bar
ENV POSTGRES_DBNAME TSM
ENV ALLOW_IP_RANGE 0.0.0.0/0

FROM your-image
USER root
RUN mkdir -p /data \
 && chown -R root /data
USER root

RUN psql -h 0.0.0.0 -d TSMDEV -U foo --file=/tmp/data/load_data.sql
