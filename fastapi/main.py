import uvicorn
from fastapi import FastAPI
from app.routers import stock

from dotenv import load_dotenv

app = FastAPI()

app.include_router(stock.router)

load_dotenv()


@app.get("/")
def root():
    return {"message": "Stock Price Prediction API"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
