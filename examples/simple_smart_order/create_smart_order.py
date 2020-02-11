from ccai.client import Client

def test_create_smart_order():
  # create simple smart order that will entry by market and exit with 15% profit
  # or exit at 10% loss

  client = Client('SECRET',
                  'KEYID')
  smart_order = {
    "marketType": 1, # 0 - spot, 1 - futures
    "pair": "BTC_USDT",
    "stopLoss": 10.0, # 7% loss
    "stopLossType": "market", # will place stop-limit or stop-market
    "leverage": 30, # leverage
    "entryOrder": {
      "side": "buy",
      "orderType": "market",
      "type": 0, # not using yet, just place 0
      "amount": 0.01 # btc amount
    },
    "exitLevels": [
      {
        "price": 15, # 15% profit
        "amount": 100, # 70% from entry
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

