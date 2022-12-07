from fastapi import APIRouter

from app.schemas.stock import StockInfo

router = APIRouter(prefix="/stock")


@router.post("/")
def predict_stock_price(stock_info: StockInfo) -> float:
    """전날 주가 정보를 입력받아 model prediction 결과(=다음날 종가)를 반환합니다.
    Args:
        stock_info (StockInfo): open, high, low, close, volume 정보
    Returns:
        float: 다음날 종가
    """
    pass
