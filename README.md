## Cryptocurrencies.AI API python client

### How to generate api key and keyId?

Go to your profile api page: https://app.cryptocurrencies.ai/profile/api <br/>
Click on "GENERATE API KEY" <br/>
How to copy KeyId: <br/>
Go to your profile accounts page: https://app.cryptocurrencies.ai/profile/accounts <br/>
Click on copy icon -> your key token will be copied in clipboard

## Reference

Some methods require 'params' dict

```
param = {
    "strategyId": "5ded5307240b81f3012372de"
}
status = client.get_order_status(params=param)
```

### get_order_status
Args: ('params' dict)  
&nbsp;&nbsp;strategyId (str): order id

Returns:  
&nbsp;&nbsp;string: order status [Waiting, Canceled]

### create_order

Args:  
&nbsp;&nbsp;marketType (int): 0 for spot, 1 for futures market  
&nbsp;&nbsp;pair (str): currency pair with underscore, e.g. "BTC_USDT"  
&nbsp;&nbsp;stopLoss (float): stop loss percent, e.g. 10.0  
&nbsp;&nbsp;stopLossType (str): stop loss type [limit, market]  
&nbsp;&nbsp;leverage (int): leverage [1 - 125]  
&nbsp;&nbsp;entryOrder (dict):  
&nbsp;&nbsp;side (str): [buy, sell]  
&nbsp;&nbsp;orderType (str): [limit, market]  
&nbsp;&nbsp;type (int): not using yet, just place 0  
&nbsp;&nbsp;amount (float): coin amount, e.g. 0.01  
&nbsp;&nbsp;exitLevels (dict array): one or more exit levels {  
&nbsp;&nbsp;&nbsp;&nbsp;type (int): 1 - amount and price is in percentage, 0 - in absolute values [0, 1]  
&nbsp;&nbsp;&nbsp;&nbsp;price (float): percent of profit, e.g. 15, or absolute price (depending of type)  
&nbsp;&nbsp;&nbsp;&nbsp;amount (int): percent of entry, e.g. 70, or absolute amount (depending of type)  
&nbsp;&nbsp;&nbsp;&nbsp;orderType (string): order type, e.g. "limit"  
&nbsp;&nbsp;}

Returns:  
&nbsp;&nbsp;dict: order info

### cancel_order
Args: ('params' dict)  
&nbsp;&nbsp;strategyId (str): order id

Returns:  
&nbsp;&nbsp;string: order state

### get_active_smart_orders
Args:  
&nbsp;&nbsp;marketType (int): 0 for spot, 1 for futures market  

Returns:  
&nbsp;&nbsp;dict array: array of active smart orders

### get_active_smart_orders_ids
Convenient wrapper for get_active_smart_orders which returns only smart order ids  
Args:  
&nbsp;&nbsp;marketType (int): 0 for spot, 1 for futures market  

Returns:  
&nbsp;&nbsp;string array: array of active smart orders ids

### get_balances
Args:  
&nbsp;&nbsp;none

Returns:  
&nbsp;&nbsp;dict array: balances for all assets  
&nbsp;&nbsp;example: [{'assetType': 0, 'locked': 0, 'free': 31.86915117, 'asset': {'symbol': 'USDT', 'priceUSD': 1}}]

### get_futures_free_balance
Convenient wrapper for get_balances.  
Args:  
&nbsp;&nbsp;symbol (str): coin symbol, e.g. USDT

Returns:  
&nbsp;&nbsp;float: coin balance on futures wallet


    
    
