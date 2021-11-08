import requests
from SECRET import API_KEY_COINMARKETCAP

class CryptoPriceCommand:

    def __init__(self):
        self.help = """Use as \\crypto-price <symbol>, for example: \\crypto-price BNB"""

    def __call__(self, params):
        symbol = params.split("-")[-1].upper()
        price = self.get_price(symbol)
        if price:
            return [
                {"type": "text", "text": "{} price is: {} USD".format(symbol, price)},
            ]
        else:
            return [
                {"type": "text", "text": "Crypto price command recognized. Data acquisition failed."},
            ]

    def get_price(self, symbol):
        try:
            url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
            headers = {"X-CMC_PRO_API_KEY": API_KEY_COINMARKETCAP,}
            parameters = {"symbol": symbol}
            r = requests.get(url, headers=headers, params=parameters)
            return r.json()["data"][symbol]["quote"]["USD"]["price"]
        except:
            return False




if __name__ == "__main__":
    get_price("BTC")
