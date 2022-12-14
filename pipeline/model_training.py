import sys
from datetime import datetime, timedelta

import pandas as pd
from prefect import flow, task, get_run_logger
from sqlalchemy import create_engine
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_squared_log_error,
    mean_absolute_error,
    mean_squared_error,
)

from settings import Settings


@task
def create_db_engine(HOST_URL):
    engine = create_engine(HOST_URL)
    return engine


@task
def read_data_from_database(query, engine):
    return pd.read_sql_query(query, con=engine)


@task
def preprocessing(train_df, valid_df, country):
    features = ["Open", "High", "Low", "Close", "Volume"]
    scaler = MinMaxScaler()

    train_df = train_df[train_df["company_name"] == country].copy().reset_index()
    valid_df = valid_df[valid_df["company_name"] == country].copy().reset_index()

    train_df["TomorrowClosePrice"] = train_df["Close"].shift(-1)
    train_df.dropna(axis=0, inplace=True)
    train_feature_df = train_df[features]

    train_X = scaler.fit_transform(train_feature_df)
    train_Y = train_df["TomorrowClosePrice"]

    valid_Y = valid_df["Close"].shift(-1)
    valid_Y.rename("TomorrowClosePrice", inplace=True)
    valid_feature_df = valid_df[features]
    valid_X = scaler.transform(valid_feature_df)

    return train_X, train_Y, valid_X, valid_Y


@task
def train_model(train_X, train_Y):
    model = LinearRegression()
    model.fit(train_X, train_Y)

    return model


@task
def create_prediction_info(model, valid_X, valid_Y):
    pred = pd.Series(model.predict(valid_X))
    df = pd.concat([valid_Y, pred], axis=1, ignore_index=True)
    df.columns = ["TomorrowClosePrice", "PredictionResult"]
    last_day_prediction = df["PredictionResult"].iloc[-1]
    df.dropna(inplace=True)
    msle = mean_squared_log_error(df["TomorrowClosePrice"], df["PredictionResult"])
    mae = mean_absolute_error(df["TomorrowClosePrice"], df["PredictionResult"])
    mse = mean_squared_error(df["TomorrowClosePrice"], df["PredictionResult"])

    info_dict = {
        "msle": msle,
        "mae": mae,
        "mse": mse,
        "last_day_prediction_result": last_day_prediction,
    }

    return info_dict


@task
def save_data(*args):
    logger = get_run_logger()
    for arg in args:
        logger.info(arg)


@flow
def train_model_flow(train_df, valid_df, country_list, date):
    for country in country_list:
        train_X, train_Y, valid_X, valid_Y = preprocessing(train_df, valid_df, country)
        model = train_model(train_X, train_Y)
        info_dict = create_prediction_info(model, valid_X, valid_Y)
        save_data(country, date, info_dict, train_X.shape, valid_X.shape)


@flow
def training_flow(date):
    if date == "daily":
        date = str((datetime.today() + timedelta(hours=9) - timedelta(days=30)).date())

    HOST_URL = Settings.POSTGRES_HOST
    TRAIN_QUERY = f"""
        SELECT * FROM stocktable WHERE "Date" < '{date}'
    """
    VALID_QUERY = f"""
        SELECT * FROM stocktable WHERE "Date" >= '{date}' 
    """

    COUNTRY_LIST = ["APPLE", "GOOGLE", "MICROSOFT", "AMAZON"]
    engine = create_db_engine(HOST_URL)
    train_df = read_data_from_database(TRAIN_QUERY, engine)
    valid_df = read_data_from_database(VALID_QUERY, engine)
    train_model_flow(train_df, valid_df, COUNTRY_LIST, date)


if __name__ == "__main__":
    date = sys.argv[1] if len(sys.argv) > 1 else "daily"

    training_flow(date)
