from pydantic import BaseModel, Field


class StockInfo(BaseModel):
    """
    API로 입력받는 데이터들의 필수 입력 여부, 자료형, 최소-최대길이,
    최소-최대값 등 여러 제한사항을 지정할 수 있습니다.
    """

    open: float = Field(..., ge=0)
    high: float = Field(..., ge=0)
    low: float = Field(..., ge=0)
    close: float = Field(..., ge=0)
    volume: int = Field(..., ge=0)

    class Config:  # swagger에서 보여줄 각 파라미터에 대한 예시를 설정할 수 있습니다.
        schema_extra = {
            "example": {
                "open": 95.37000274658203,
                "high": 96.97000122070312,
                "low": 94.02999877929688,
                "close": 94.8499984741211,
                "volume": 82617900,
            }
        }
