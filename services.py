from decimal import Decimal

import httpx
from fastapi import Depends

from config import Settings, get_settings
from exceptions import APIConnectionError


class ExchangeRateAPIService:
    def __init__(self, settings: Settings = Depends(get_settings)) -> None:
        self.API_KEY = settings.EXCHANGE_RATE_API_KEY
        self.URL = settings.EXCHANGE_RATE_API_URL
        self.CURRENCY_BASE = settings.EXCHANGE_RATE_API_BASE

    def get_rates(self) -> dict[str, Decimal]:
        try:
            params = {
                'app_id': self.API_KEY,
                'base': self.CURRENCY_BASE,
                'show_alternative': True,  # retorna moedas que ainda não foram liberadas oficialmente na API, como o ETH  # noqa
            }
            response = httpx.get(url=f'{self.URL}/latest.json', params=params)
            response.raise_for_status()
            return response.json()['rates']
        except httpx.HTTPError as exc:
            raise APIConnectionError() from exc


class CurrencyConversionService:
    def __init__(
        self, rate_service: ExchangeRateAPIService = Depends()
    ) -> None:
        self.rate_service = rate_service

    def convert(
        self, from_currency: str, to_currency: str, amount: Decimal
    ) -> Decimal:
        rates = self.rate_service.get_rates()
        rate_from = Decimal(rates.get(from_currency))
        rate_to = Decimal(rates.get(to_currency))
        return amount / rate_from * rate_to
