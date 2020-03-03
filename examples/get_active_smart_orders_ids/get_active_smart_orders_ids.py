from ccai.client import Client

def test_get_active_smart_orders_ids():
  client = Client('apisecret', 'keyid')
  # available market types: 0 - spot, 1 - futures
  marketType = 1
  response = client.get_active_smart_orders_ids(marketType)
  print("IDs of currently active SMs:", response)