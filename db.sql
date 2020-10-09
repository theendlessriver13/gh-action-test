CREATE TABLE test (
    a INT,
    b DOUBLE PRECISION,
    c TEXT
);

INSERT INTO test (a, b, c)
    VALUES (5, 1.2, 'This is Text');

SELECT * FROM test;
