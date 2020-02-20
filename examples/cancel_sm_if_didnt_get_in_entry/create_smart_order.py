from ccai.client import Client

def test_create_smart_order():
  #  create smart order that will
  #  cancel if didnt get into entry

  client = Client('SECRET',
                  'KEYID')
  smart_order = {
    "marketType": 1,  # 0 - spot, 1 - futures
    "pair": "BTC_USDT",
    "stopLoss": 10.0,  # 10% loss
    "stopLossType": "limit",  # will place stop-limit or stop-market for stop-loss
    "leverage": 125,  # leverage
    "waitingEntryTimeout": 100,   # if didnt get in entry for 100 seconds - cancel SM
    "activationMoveStep": 1,      # move activatePrice 1% closed
    "activationMoveTimeout": 5,   # waiting 5 seconds before moving activatePrice
    "entryOrder": {
      "side": "buy",
      "orderType": "market",
      "activatePrice": 9950,
      "entryDeviation": 15,
      "type": 0,  # not using yet, just place 0
      "amount": 0.001  # btc amount (after leverage)
    },
    "exitLevels": [
      {
        "price": 8, # 8% profit
        "amount": 40, # 40% from entry
        "type": 1, # 1 - means amount and price is in percentage
        "orderType": "limit"
      }
    ]
  }
  response = client.create_order(params=smart_order)
  print(response)

test_create_smart_order()

