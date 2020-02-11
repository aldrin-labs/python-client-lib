from ccai.client import Client

def test_create_smart_order():
  # create smart order that will
  # entry with market order
  # set take-profit targets at 8% profit with 40% of amount and 15% with 60% of amount
  # set stop-loss at 10%

  client = Client('SECRET',
                  'KEYID')
  smart_order = {
    "marketType": 1,  # 0 - spot, 1 - futures
    "pair": "BTC_USDT",
    "stopLoss": 10.0,  # 10% loss
    "stopLossType": "limit",  # will place stop-limit or stop-market for stop-loss
    "leverage": 125,  # leverage
    "entryOrder": {
      "side": "buy",
      "orderType": "market",
      "type": 0,  # not using yet, just place 0
      "amount": 0.01  # btc amount (after leverage)
    },
    "exitLevels": [
      {
        "price": 8, # 8% profit
        "amount": 40, # 40% from entry
        "type": 1, # 1 - means amount and price is in percentage
        "orderType": "limit"
      },
      {
        "price": 15, # 15% profit
        "amount": 60, # 60% from entry
        "type": 1, # 1 - means amount and price is in percentage
        "orderType": "limit"
      }
    ]
  }
  response = client.create_order(params=smart_order)
  print(response)

def test_get_balances():
  client = Client('apisecret', 'keyid')
  response = client.get_balances()
  print(response)

#test_create_smart_order()
#test_get_balances()
test_create_smart_order()

