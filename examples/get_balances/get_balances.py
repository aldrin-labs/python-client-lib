from ccai.client import Client

def test_get_balances():
  client = Client('apisecret', 'keyid')
  response = client.get_balances()
  print(response)