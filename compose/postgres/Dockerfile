FROM docker.io/postgres:16-bookworm

RUN apt-get update && apt-get install -y gnupg2
RUN apt-get install -y postgis postgresql-16-postgis-3

COPY ./compose/postgres/maintenance /usr/local/bin/maintenance
#COPY ./compose/postgres/postgresql.conf /etc/postgresql/postgresql.conf

RUN chmod +x /usr/local/bin/maintenance/*
RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
    && rmdir /usr/local/bin/maintenance

#CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]
