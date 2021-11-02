import requests
from SECRET import API_KEY_COINMARKETCAP

def crypto_price(params):
    symbol = params.split("-")[-1].upper()
    price = get_price(symbol)
    if price:
        return [
            {"type": "text", "text": "{} price is: {} USD".format(symbol, price)},
        ]
    else:
        return [
            {"type": "text", "text": "Crypto price command recognized. Data acquisition failed."},
        ]

def get_price(symbol):
    try:
        url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
        API_KEY = "37756f2b-416e-49d1-9f2b-54915e04e182"
        headers = {"X-CMC_PRO_API_KEY": API_KEY_COINMARKETCAP,}
        parameters = {"symbol": symbol}
        r = requests.get(url, headers=headers, params=parameters)
        return r.json()["data"][symbol]["quote"]["USD"]["price"]
    except:
        return False


if __name__ == "__main__":
    get_price("BTC")
