
import collections   
def check_btc(data):
    res = []
    q = collections.deque()
    
    for item in data:
        if item["type"] == "buy":
            q.append(item)
            
        elif item["type"] == "sell":
            
            n = item["amount"]
            while n > 0:
                cur_unit_price = item["price"] / item["amount"]

                if q[0]["amount"] > n:
                    
                    buy_unit_price = q[0]["price"] / q[0]["amount"]
                    
                    cost_basis = n * buy_unit_price
                    proceeds = n * cur_unit_price
                    gain = proceeds - cost_basis
                    amount = n
                    
                    q[0]["amount"] = q[0]["amount"] - n
                    q[0]["price"] = q[0]["price"] - cost_basis
                    
                    result = "Sell" + "(date=" + item["date"] + ",date_acquired=" + q[0]["date"] + ")"
                    res.append(result)
                    
                else:
                    cur = q.popleft()
                    buy_unit_price = cur["price"] / cur["amount"]
                    cost_basis = cur["amount"] * buy_unit_price
                    proceeds = cur["amount"] * cur_unit_price
                    gain = proceeds - cost_basis
                    amount = cur["amount"]
                    result = "Sell" + "(date=" + item["date"] + ",date_acquired=" + q[0]["date"] + ")"
                    res.append(result)
                n = n - cur["amount"]
    return res
                

                
            
            
            
            
 
    
    
# date, date_acquired, cost_basis, proceeds, gain, amount
# amount 5, unit pirce 5
# amount 10, unit pirce 4
## amount 7, unit pirce 6 : # amount 5, unit pirce 5, amount 2, unit pirce 4
# remaining, res
            




input = [
    {
      "date": 1,
      "type": "buy",
      "price": 25,
      "amount": 5. // each BTC = $5  (  7*5 = $35; 7*4=$28; -$7 )
    },{
      "date": 2,
      "type": "buy",
      "price": 40,
      "amount": 10
    },{
      "date": 3,
      "type": "sell",
      "price": 42,
      "amount": 7
    },{
      "date": 4,
      "type": "sell",
      "price": 3,
      "amount": 1
    },{
      "date": 5,
      "type": "buy",
      "price": 25,
      "amount": 5
    },{
      "date": 6,
      "type": "sell",
      "price": 20,
      "amount": 10
    }
    ]