from decimal import Decimal

from fastapi import FastAPI, Query

from enums import CurrencyCode

app = FastAPI(
    title="Currency Converter",
    description="Uma API REST para conversão de moedas",
    version="1.0.0",
)


@app.get("/conversions")
def convert(
    from_currency: CurrencyCode = Query(..., alias='from'),
    to_currency: CurrencyCode = Query(..., alias='to'),
    amount: Decimal = Query(..., ge=0),
):
    return {
        "result": "test",
        'from': from_currency,
        'to': to_currency,
        'amount': amount,
    }
