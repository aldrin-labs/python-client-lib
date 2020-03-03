from ccai.client import Client

def test_get_active_smart_orders():
  client = Client('apisecret', 'keyid')
  # available market types: 0 - spot, 1 - futures
  marketType = 1
  response = client.get_active_smart_orders(marketType)
  print("Currently active SMs:", response)