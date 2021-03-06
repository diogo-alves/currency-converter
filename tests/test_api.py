from itertools import product
from numbers import Number

import pytest
from fastapi import status

from app.api import router
from app.enums import CurrencyCode


@pytest.fixture
def url():
    return router.url_path_for('convert')


@pytest.mark.parametrize(
    'from_currency, to_currency', product(CurrencyCode, repeat=2)
)
def test_convert_with_valid_currency_combinations(
    client, url, from_currency, to_currency
):
    params = {'from': from_currency, 'to': to_currency, 'amount': 0}
    response = client.get(url, params=params)
    assert response.status_code == status.HTTP_200_OK


def test_convert_when_parameter_from_is_invalid(client, url):
    params = {'from': 'JPY', 'to': CurrencyCode.EUR, 'amount': 0}
    response = client.get(url, params=params)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_convert_when_parameter_to_is_invalid(client, url):
    params = {'from': CurrencyCode.BRL, 'to': 'ARS', 'amount': 0}
    response = client.get(url, params=params)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_convert_when_parameter_amount_is_invalid(client, url):
    params = {'from': CurrencyCode.BRL, 'to': CurrencyCode.EUR, 'amount': -1}
    response = client.get(url, params=params)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_convert_should_return_any_type_of_number(client, url):
    params = {'from': CurrencyCode.USD, 'to': CurrencyCode.USD, 'amount': 1}
    response = client.get(url, params=params)
    assert isinstance(response.json()['result'], Number)
