from fastapi import FastAPI

app = FastAPI(
    title="Currency Converter",
    description="Uma API REST para conversão de moedas",
    version="1.0.0",
)


@app.get("/")
def convert():
    return {"result": "test"}
