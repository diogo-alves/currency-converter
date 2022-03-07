from decimal import Decimal

from fastapi import FastAPI, Query, Request, status
from fastapi.responses import JSONResponse

from enums import CurrencyCode
from exceptions import APIConnectionError
from schemas import ConversionResponse

app = FastAPI(
    title="Currency Converter",
    description="Uma API REST para conversão de moedas",
    version="1.0.0",
)


@app.exception_handler(APIConnectionError)
def api_connection_exception_handler(
    request: Request,
    exc: APIConnectionError,
):
    return JSONResponse(
        status_code=status.HTTP_502_BAD_GATEWAY,
        content={'detail': 'Falha na comunicação com o servidor remoto.'},
    )


@app.get("/conversions", response_model=ConversionResponse)
def convert(
    from_currency: CurrencyCode = Query(..., alias='from'),
    to_currency: CurrencyCode = Query(..., alias='to'),
    amount: Decimal = Query(..., ge=0),
) -> ConversionResponse:
    return ConversionResponse(result=1)
