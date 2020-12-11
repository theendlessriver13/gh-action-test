SELECT name FROM pg_available_extensions;

SELECT extname, extversion FROM pg_extension;

CREATE EXTENSION IF NOT EXISTS timescaledb;

CREATE TABLE test (
    date TIMESTAMP,
    b DOUBLE PRECISION,
    c TEXT
);

SELECT create_hypertable('test', 'date');


INSERT INTO test (date, b, c)
    VALUES ('2020-10-31 15:18:00', 1.2, 'This is Text');

SELECT * FROM test;
