from ccai.client import Client

def test_create_smart_order():
  # trailing entry -> trailing take profit

  client = Client('SECRET',
                  'KEYID')
  smart_order = {
    "marketType": 1, # 0 - spot, 1 - futures
    "pair": "BTC_USDT",
    "stopLoss": 10.0, # 7% loss
    "stopLossType": "limit", # will place stop-limit or stop-market
    "leverage": 30, # leverage
    "entryOrder": {
      "side": "buy",
      "orderType": "limit",
      "type": 0, # not using yet, just place 0
      "amount": 0.01, # btc amount
    },
    "exitLevels": [
      {
        "amount": 100, # 70% from entry
        "activatePrice": 10,  # will start trailing and follow the trend after 10% profit
        "entryDeviation": 5,  # exit on 5% rebounce
        "type": 1, # 1 - means amount and price is in percentage
        "orderType": "market"
      },
    ]
  }
  response = client.create_order(params=smart_order)
  print(response)

def test_get_balances():
  client = Client('apikey', 'keyid')
  response = client.get_balances()
  print(response)

#test_create_smart_order()
#test_get_balances()
test_create_smart_order()

