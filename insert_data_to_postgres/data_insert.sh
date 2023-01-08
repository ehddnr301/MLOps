#!/bin/bash
docker cp stock.csv postgresql:/

docker exec -it postgresql\
 psql \
 -U postgres \
 -d postgres \
 -c "CREATE TABLE STOCK_PRICE (
    DATE DATE NULL,
    Open FLOAT NULL,
    High FLOAT NULL,
    Low FLOAT NULL,
    Close FLOAT NULL,
    AdjClose FLOAT NULL,
    Volume BIGINT NULL,
    Company_name VARCHAR(20) NULL
 )"
 
docker exec -it postgresql\
 psql \
 -U postgres \
 -d postgres \
 -c "COPY STOCK_PRICE FROM '/stock.csv' WITH (FORMAT csv, header)"
