import pytest

from config import Settings
from enums import CurrencyCode
from exceptions import APIConnectionError
from services import ExchangeRateAPIService


@pytest.fixture
def rate_service(test_settings) -> ExchangeRateAPIService:
    return ExchangeRateAPIService(test_settings)


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
