from decimal import Decimal

import pytest

from config import Settings
from enums import CurrencyCode
from exceptions import APIConnectionError
from services import CurrencyConversionService, ExchangeRateAPIService


@pytest.fixture
def rate_service(test_settings) -> ExchangeRateAPIService:
    return ExchangeRateAPIService(test_settings)


@pytest.fixture
def conversion_service(rate_service) -> CurrencyConversionService:
    return CurrencyConversionService(rate_service)


class TestExchangeRateAPIService:
    def test_get_rates_should_return_dict_with_rates(self, rate_service):
        rates = rate_service.get_rates()
        assert isinstance(rates, dict)
        assert rates

    def test_get_rates_return_all_permitted_currencies(self, rate_service):
        rates = rate_service.get_rates()
        assert all(currency in rates.keys() for currency in CurrencyCode)

    def test_invalid_api_key(self):
        settings = Settings(EXCHANGE_RATE_API_KEY='')
        rate_service = ExchangeRateAPIService(settings)
        with pytest.raises(APIConnectionError):
            rate_service.get_rates()


class TestCurrencyConversionService:
    def test_conversion(self, conversion_service, mocker):
        mocker.patch.object(
            conversion_service.rate_service,
            'get_rates',
            return_value={CurrencyCode.USD: 1, CurrencyCode.BRL: 5.05822},
        )
        result = conversion_service.convert(
            from_currency=CurrencyCode.USD,
            to_currency=CurrencyCode.BRL,
            amount=10,
        )
        assert pytest.approx(result) == Decimal(50.5822)
