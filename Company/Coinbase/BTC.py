"""
一堆交易BTC的记录

output：
Sell(date: 3, date_acquire=1, amount= 5, proceeds=30.0, gain=6.0)
Sell(date: 3, date_acquire=2, amount= 2, proceeds=12.0, gain‍‍‌‍‌‌‍‍‌‍‌‍‌‌‍‍‍‌‌‍=2.0)
……
打印完全部的sell，如果还有剩余，就把余额打出来
类似 Buy(date: 6, date_acquire=N, amount= N, price=N)
注意在处理第三天的卖的时候，虽然把第一天买的BTC卖完了，但是第二天的还有剩余，需要更新第二天的记录，下次卖的时候再处理
一看是新题有点懵，中间算proceeds和gain把自己弄晕了，最后到时间了，还有bug，肯定挂了

"""

"""
date: 3, date_acquire=2, amount=2, proceeds=12.0, gain‍‍‌‍‌‌‍‍‌‍‌‍‌‌‍‍‍‌‌‍=2.0
"""
import heapq
# class Btc(object):
#     def __init__(self) -> None:
#         self.heap = []
#         self.date_acquire = None
#         self.amount = None
#         self.proceeds = None
#         self.gain = None
#
#     def buy(self, price):
#         pass
#     def sell(self, price):
#         pass

import heapq
def check_btc(data):
    res = []
    heap = []
    date_acquire = None
    amount = None
    proceeds = None
    gain = None

    for item in input:
        if item['type'] == "sell":

            if not heap:
                return "No stock to sell"

            numbers_to_sell = item['amount']
            while numbers_to_sell > 0 and heap:
                cur_unit_price = item['price'] / item['amount']
                unit_price, shares, date = heapq.pop():

                date_acquire = date
                amount = min(shares, numbers_to_sell)

                # gain = 5 * （42 / 7 - 25 / 5）
                gain ‍‍‌‍‌‌‍‍‌‍‌‍‌‌‍‍‍‌‌‍= (cur_unit_price - unit_price) * amount
                proceeds += gain

                cur_res = [date_acquire, amount, proceeds, gain]
                res.append(cur_res)

                numbers_to_sell -= item['amount']
                if numbers_to_sell <= 0:
                    heapq.heappush(heap, [unit_price, shares - numbers_to_sell, date])
            res.append()
        elif item['type'] == "buy":
            # {'date': 1, 'amount': 5, 'price': 25.0, 'type': 'buy'}
            unit_price = item['price'] / item['amount']
            shares = item['amount']
            date = item['date']
            # [单价，数量, 日期]
            heapq.heappush(heap,[unit_price, shares, date])


input = [{"date": 1, "amount": 5, "price": 25.0, "type": "buy"},
{"date": 2,
"amount" : 20,
"price": 60.0,
"type": "buy"
},
{"date": 3,
"amount" : 7,
"price": 42.0,
"type": "sell"
},
{"date": 4,
"amount" : 6,
"price": 30.0,
"type": "sell"
},
{"date": 5,
"amount" : 5,
"price": 25.0,
"type": "buy"
},
{"date": 6,
"amount" : 5,
"price": 25.0,
"type": "buy"
}]

