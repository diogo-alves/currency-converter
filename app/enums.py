from enum import Enum


class CurrencyCode(str, Enum):
    USD = 'USD'
    BRL = 'BRL'
    EUR = 'EUR'
    BTC = 'BTC'
    ETH = 'ETH'
