from decimal import Decimal

from pydantic import BaseModel


class ConversionResponse(BaseModel):
    result: Decimal
