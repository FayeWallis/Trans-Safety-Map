CREATE TABLE INCIDENTS
(
    CITY VARCHAR,
    STATE CHAR(2),
    YEAR INT,
    SEVERITY VARCHAR
);

COPY INCIDENTS FROM '/run/data/summary_data.csv' WITH (FORMAT csv, HEADER TRUE);