from ccai.client import Client

def test_create_smart_order():
  # create SM that will go into entry
  # and place 3 targets
  # stop-loss at 7% loss from entry price

  client = Client('SECRET',
                  'KEYID')
  smart_order = {
    "marketType": 1,  # 0 - spot, 1 - futures
    "pair": "BTC_USDT",
    "stopLoss": 7.0,  # 7% loss
    "stopLossType": "limit",  # will place stop-limit or stop-market
    "leverage": 125,  # leverage
    "entryOrder": {
      "side": "buy",
      "orderType": "market",
      "type": 0,  # not using yet, just place 0
      "activatePrice": 9120,  # start into trailing once price crosses 9120
      "entryDeviation": 5,  # buy on 5% rebounce
      "amount": 0.01  # btc amount
    },
    "exitLevels": [
      {
        "price": 15,  # 15% profit
        "amount": 30,  # 70% from entry
        "type": 1,  # 1 - means amount and price is in percentage
        "orderType": "limit"
      },
      {
        "price": 25,  # 15% profit
        "amount": 30,  # 30% from entry
        "type": 1,  # 1 - means amount and price is in percentage
        "orderType": "limit"
      },
      {
        "price": 30,  # 30% profit
        "amount": 40,  # 30% from entry
        "type": 1,  # 1 - means amount and price is in percentage
        "orderType": "market"
      }
    ]
  }
  response = client.create_order(params=smart_order)
  print(response)

def test_get_balances():
  client = Client('apisecret', 'keyid')
  response = client.get_balances()
  print(response)

test_create_smart_order()

