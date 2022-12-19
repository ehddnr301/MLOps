import mlflow

from fastapi import APIRouter
from app.schemas.stock import StockInfo

import numpy as np

router = APIRouter(prefix="/stock")


@router.post("/")
def predict_stock_price(stock_info: StockInfo) -> float:
    """전날 주가 정보를 입력받아 model prediction 결과(=다음날 종가)를 반환합니다.
    Args:
        stock_info (StockInfo): open, high, low, close, volume 정보
    Returns:
        float: 다음날 종가
    """
    MODEL_NAME = "stock"
    MODEL_STAGE = "Production"

    model_uri2 = f"models:/{MODEL_NAME}/{MODEL_STAGE}"

    model = mlflow.sklearn.load_model(model_uri2)
    data = np.reshape(np.array(list(stock_info.dict().values())), (1, -1))
    res = model.predict(data)

    return float(res[0])
