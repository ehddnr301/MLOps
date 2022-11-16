import os
import argparse

import psycopg2
import pandas as pd
from sqlalchemy import create_engine

from settings import Settings


if __name__ == "__main__":
    DEFAULT_FILE_PATH = f"{os.getcwd()}/stock.csv"
    DEFAULT_TABLE_NAME = "stocktable"

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path", "-p", help="파일 경로를 입력해주세요.", type=str, default=DEFAULT_FILE_PATH
    )
    parser.add_argument(
        "--table", "-t", help="테이블 이름을 입력해주세요.", type=str, default=DEFAULT_TABLE_NAME
    )
    args = parser.parse_args()

    PATH: str = args.path
    TABLE_NAME: str = args.table

    if not os.path.isfile(PATH):
        raise Exception("해당경로에 파일이 존재하지 않습니다.")

    if not TABLE_NAME.isalnum():
        raise Exception("테이블명에 특수문자를 포함하지 말아주세요.")

    # Create Engine (Not Actual Connection)
    engine = create_engine(Settings.POSTGRES_HOST)

    # Insert Data
    df = pd.read_csv(PATH)
    df.to_sql(TABLE_NAME, con=engine, if_exists="replace", index=False)
