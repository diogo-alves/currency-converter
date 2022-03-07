from decimal import Decimal

from fastapi import APIRouter, Depends, Query

from ..enums import CurrencyCode
from ..schemas import ConversionResponse
from ..services import CurrencyConversionService

router = APIRouter(prefix='/v1', tags=['Conversions'])


@router.get("/conversions", response_model=ConversionResponse)
def convert(
    from_currency: CurrencyCode = Query(..., alias='from'),
    to_currency: CurrencyCode = Query(..., alias='to'),
    amount: Decimal = Query(..., ge=0),
    conversion_service: CurrencyConversionService = Depends(),
) -> ConversionResponse:
    result = conversion_service.convert(from_currency, to_currency, amount)
    return ConversionResponse(result=result)
