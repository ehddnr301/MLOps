# Tutorial

## Directory Structure

```
.
├── .env
├── README.md
├── data_insert.py
├── settings.py
└── stock.csv
```

## Create DataBase

- 도커가 띄워져 있는지 확인후에 띄워져 있지 않다면 `postgres_docker.sh`파일을 실행시켜 줍니다.

- `docker exec -it postgresql bash`
- `psql -U postgres`
- `create database something;`
- `\c something`

## Create .env file

- ADD `POSTGRES_HOST=postgresql://postgres:postgres@127.0.0.1:5432/something`

## Insert Data

### Case1

- `stock.csv` 파일을 사용할 경우
  - `python data_insert.py`

### Case2

- 자신의 csv파일을 사용할 경우
  - `python data_insert.py --path {파일경로} --table {테이블명}`
  - ex) `python data_insert.py --path ~/insert_data_to_postgres/stock.csv --table sample`