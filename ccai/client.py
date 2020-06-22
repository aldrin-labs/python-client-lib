from six.moves import urllib
import json

class Client(object):
  API_URL = 'https://api.cryptocurrencies.ai/graphql'

  def __init__(self, api_key=None, key_id = ""):
    """CCAI API Client constructor
    :param api_key: Api Key you generated
    """

    self.API_KEY = api_key
    self.keyId = key_id
    self.response = None

  # returns string, for example "Waiting"
  def get_order_status(self, **params):
    query = "query getStrategyStatus($input: getStrategyStatusInput!){\n  getStrategyStatus(input: $input)\n}"
    params["params"]["accountId"] = self.keyId
    mutation_params = {}
    mutation_params["keyId"] = self.keyId
    mutation_params["strategyId"] = params["params"]["strategyId"]
    params = {
      "input": mutation_params
    }

    try:
      response = self._send(query, variables=params)
      return json.loads(response)["data"]["getStrategyStatus"]
    except:
      print('Exception occurred')

  # returns state of order
  def cancel_order(self, **params):
    query = "mutation disableStrategy($input: disableStrategyInput!) {\n    disableStrategy(input: $input) {\n      state {\n        state\n      }\n    }\n}"
    params["params"]["accountId"] = self.keyId
    mutation_params = {}
    mutation_params["keyId"] = self.keyId
    mutation_params["strategyId"] = params["params"]["strategyId"]
    params = {
      "input": mutation_params
    }
    try:
      response = self._send(query, variables=params)
      return json.loads(response)["data"]["disableStrategy"]["state"]
    except:
      print('Exception occurred')

  # returns new order id as string, for example "5e2b08dd1a1f278b0c2084e9"
  def create_order(self, **params):
    query = "mutation createOrder($keyId: String!, $keyParams: createOrderParams!) {\n  createOrder(keyId: $keyId, keyParams: $keyParams) {\n    status\n    orderId\n }\n}\n"
    params["params"]["accountId"] = self.keyId
    mutation_params = {}
    mutation_params["keyId"] = self.keyId
    mutation_params["keyParams"] = {
      "type": "smart",
      "params": {"smartOrder": params["params"]},
      "symbol": "0", # остальные поля не нужны но обязательны (поправлю в апи потом)
      "amount": 0,
      "side": "0",
    }
    response = self._send(query, variables=mutation_params)
    decoded = json.loads(response)

    try:
      if (decoded["data"] != None) and (decoded["data"]["createOrder"] != None):
        if decoded["data"]["createOrder"]["status"] == "OK":
          return decoded["data"]["createOrder"]["orderId"]

      if decoded["errors"] != None and len(decoded["errors"]) > 0:
        if decoded["errors"][0]["message"]:
          return "Server err message: " +  decoded["errors"][0]["message"]

      return "ERR"
    except:
      return "ERR"

  '''
    returns array of balances for all key assets. For example:
    [
     {'assetType': 0, 'locked': 0, 'free': 31.86915117, 'asset': {'symbol': 'USDT', 'priceUSD': 1}},
     {'assetType': 1, 'locked': 4.4637389899999995, 'free': 3.12550607, 'asset': {'symbol': 'USDT', 'priceUSD': 1}},
     {'assetType': 0, 'locked': 0, 'free': 3.1e-07, 'asset': {'symbol': 'BTC', 'priceUSD': 8471.26}}, 
     {'assetType': 1, 'locked': 0, 'free': 0, 'asset': {'symbol': 'BNB', 'priceUSD': 17.3495}},
     {'assetType': 0, 'locked': 0, 'free': 0, 'asset': {'symbol': 'BCH', 'priceUSD': 0}}, 
     {'assetType': 0, 'locked': 0, 'free': 0, 'asset': {'symbol': 'ETH', 'priceUSD': 161.62}}
    ]
  '''
  def get_balances(self):
    query = "query getFunds($fundsInput: fundsInput!) {\n getFunds(fundsInput: $fundsInput) {\n assetType\n locked \n free \n asset { \n symbol \n priceUSD\n }\n }\n}\n"
    query_params = {}
    query_params["fundsInput"] = {
      "activeExchangeKey": self.keyId
    }

    try:
      response = self._send(query, variables=query_params)
      return json.loads(response)["data"]["getFunds"]
    except:
      print('Exception occurred')

  def get_futures_free_balance(self, symbol='USDT'):
    try:
      data = self.get_balances()
      symbolAsset = list(filter(lambda a: a["asset"]["symbol"] == symbol and a["assetType"] == 1, data))
      free = symbolAsset[0].get("free", 0) if len(symbolAsset) else 0
      return free
    except Exception as e:
      print('Exception message:', e)

  # returns array of smart order objects, example: [{'_id': '5e5e06a3c543275bf7a32eba'}]
  def get_active_smart_orders(self, marketType=0):
    query = "query getActiveStrategies($input: activeStrategiesInput!) {\n getActiveStrategies(activeStrategiesInput: $input) {\n  strategies {\n  _id\n  }\n}\n}\n"
    query_params = {}
    query_params["input"] = {
      "activeExchangeKey": self.keyId,
      "marketType": marketType
    }

    try:
      response = self._send(query, variables=query_params)
      return json.loads(response)["data"]["getActiveStrategies"]["strategies"]
    except Exception as e:
      print('Exception message:', e) 

  # returns array of smart order ids, example: ['5e5e06a3c543275bf7a32eba']
  def get_active_smart_orders_ids(self, marketType=0):
    try:
      smart_orders = self.get_active_smart_orders(marketType)
      ids = []
      for smart_order in smart_orders:
        ids.append(smart_order['_id'])
      return ids
    except Exception as e:
      print('Exception message:', e)

  def _send(self, query, variables):
    data = {'query': query,
            'variables': variables}
    print(json.dumps(data).encode('utf-8'))
    headers = {'Accept': 'application/json',
               'Content-Type': 'application/json'}
    headers['apikey'] = '{}'.format(self.API_KEY)

    req = urllib.request.Request(self.API_URL, json.dumps(data).encode('utf-8'), headers)
    try:
      response = urllib.request.urlopen(req)
      return response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
      print((e.read()))
      print('')
      raise e
