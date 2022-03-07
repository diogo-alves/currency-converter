from decimal import Decimal

from fastapi import APIRouter, Depends, Query, status

from ..enums import CurrencyCode
from ..schemas import ConversionResponse
from ..services import CurrencyConversionService

router = APIRouter(prefix='/v1', tags=['Conversão'])


@router.get(
    '/conversion',
    response_model=ConversionResponse,
    summary='Utiliza parâmetros pré-definidos para realizar as conversões',
    responses={
        status.HTTP_502_BAD_GATEWAY: {
            'content': {
                'application/json': {
                    'example': {
                        'detail': 'Falha na comunicação com o servidor remoto.'
                    }
                }
            },
        }
    },
)
def convert(
    from_currency: CurrencyCode = Query(..., alias='from'),
    to_currency: CurrencyCode = Query(..., alias='to'),
    amount: Decimal = Query(..., ge=0),
    conversion_service: CurrencyConversionService = Depends(),
) -> ConversionResponse:
    result = conversion_service.convert(from_currency, to_currency, amount)
    return ConversionResponse(result=result)
