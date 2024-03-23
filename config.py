import requests
import json
from config import keys

class ConvertionExceprion(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quoit: str, base: str, amount: float,):
        if quoit == base:
            raise ConvertionExceprion(f'Невозможно перевести одинаковые валюты {base}.')
        try:
            quoit_ticker = keys[quoit]
        except KeyError:
            raise ConvertionExceprion(f'Не удалось обработать валюту {quoit}.')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExceprion(f'Не удалось обработать валюту {base}.')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExceprion(f'Не удалось обработать количество {amount}.')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quoit_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]*float(amount)
        return total_base
