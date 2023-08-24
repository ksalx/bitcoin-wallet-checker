import requests


def check_balance(url: str, addresses: str) -> dict:
    try:
        return requests.get(url + addresses).json()
    except Exception as E:
        print(E)
