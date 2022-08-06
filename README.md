## Docker Setup


First, start the postGIS container. 

**Note: it is very important that you are in the main project folder so that the volume attaches to the correct folder.**

    docker run --rm -p 5432:5432 -e POSTGRES_USER=foo -e POSTGRES_PASSWORD=bar -e POSTGRES_DB=TSMDEV -v $(pwd)/database/data:/run/data --name tsm_database postgis/postgis

In a separate terminal tab, you must run the data load script.

    docker exec tsm_database psql -h 0.0.0.0 -d TSMDEV -U foo --file=/run/data/load_data.sql

If the load was sucessfull, you will see a message like this.

    CREATE TABLE
    COPY 1024