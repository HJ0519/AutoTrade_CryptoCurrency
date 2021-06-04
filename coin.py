import requests
import pprint

def get_coin_types(currency_type):
    url = "https://api.upbit.com/v1/market/all"
    querystring = {"isDetails":"false"}
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers, params=querystring)

    results = []

    for item in response.json():
        if item ["market"].startswith(currency_type):
            results.append(item)
    results = list(filter(lambda item: item["market"].startswith(currency_type), response.json()))
    return results

def get_coin_candles(market_type, unit, interval, count):
    
    url = f"https://api.upbit.com/v1/candles/{unit}/{interval}"

    querystring = {"market": market_type, "count": count}

    headers = {"Accept": "application/json"}

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()


def get_coin_ticks(market_type, count=1):
    url = "https://api.upbit.com/v1/trades/ticks"
    
    querystring = {"market":market_type, "count":count}
    
    headers = {"Accept": "application/json"}

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()

def get_coin_tickers(market_types):
    url = "https://api.upbit.com/v1/ticker"

    querystring = {"markets":market_types}

    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()

def get_coin_orderbook(market_types):
    url = "https://api.upbit.com/v1/orderbook"

    querystring = {"markets": market_types}
    
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()

# if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4)

    results = get_coin_types('KRW')
    pp.pprint('coin_types')
    pp.pprint(results)
    
    candles = get_coin_candles('KRW-BTC','minutes', 1, 10) 
    pp.pprint('candles')
    pp.pprint(candles)

    ticks = get_coin_ticks('KRW-BTC', 2)
    pp.pprint('ticks')
    pp.pprint(ticks)

    tickers = get_coin_tickers('KRW-ETH')
    pp.pprint('tickers')
    pp.pprint(tickers)

    orderbook = get_coin_orderbook('KRW-ETH,KRW-BTC')
    pp.pprint('orders')
    pp.pprint(orderbook)
    
