from itertools import product

import pytest
from fastapi import status

from enums import CurrencyCode


@pytest.mark.parametrize(
    'from_currency, to_currency', product(CurrencyCode, repeat=2)
)
def test_convert_with_valid_currency_combinations(
    client, from_currency, to_currency
):
    params = {'from': from_currency, 'to': to_currency, 'amount': 0}
    response = client.get('/conversions', params=params)
    assert response.status_code == status.HTTP_200_OK


def test_convert_when_parameter_from_is_invalid(client):
    params = {'from': 'JPY', 'to': CurrencyCode.EUR, 'amount': 0}
    response = client.get('/conversions', params=params)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_convert_when_parameter_to_is_invalid(client):
    params = {'from': CurrencyCode.BRL, 'to': 'ARS', 'amount': 0}
    response = client.get('/conversions', params=params)
    # print(response.__dict__)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_convert_when_parameter_amount_is_invalid(client):
    params = {'from': CurrencyCode.BRL, 'to': 'ARS', 'amount': -1}
    response = client.get('/conversions', params=params)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
