from decimal import Decimal

from fastapi import Depends, FastAPI, Query

from . import exceptions
from .enums import CurrencyCode
from .schemas import ConversionResponse
from .services import CurrencyConversionService

app = FastAPI(
    title="Currency Converter",
    description="Uma API REST para conversão de moedas",
    version="1.0.0",
)


@app.get("/conversions", response_model=ConversionResponse)
def convert(
    from_currency: CurrencyCode = Query(..., alias='from'),
    to_currency: CurrencyCode = Query(..., alias='to'),
    amount: Decimal = Query(..., ge=0),
    conversion_service: CurrencyConversionService = Depends(),
) -> ConversionResponse:
    result = conversion_service.convert(from_currency, to_currency, amount)
    return ConversionResponse(result=result)


@app.on_event('startup')
def startup():
    exceptions.register_exception_handler(app)
