"""
书籍买卖：要求是设计一个书籍买卖系统（包括所有的API）。开始系统就存一堆open offer to buy + open offer to sell：
-	此时如果有人想出价 X 买书， 如果当时卖书的offer最低价 < X, 则返回最低价完成交易，否则把X放进open offer to buy的pool里面
-	此时如果有人想出价 Y 卖书， 如果当时买书的offer最高价  > Y, 则返回最高价完成交易，否则把Y放进open offer to sell的pool里面。

follow up: offer to buy和sell都有时效性该怎么处理
follow up: cancel order feature怎么处理

follow up: production环境下有什么需要修改的。 需要从多个角度入手，比如检查输入变量， 用户非常多的话怎么办， 多线程的话要注意什么， 累积的buy和sell offer太多怎么办之类的。

解法：min heap and max heap, min heap is for sell offers, max heap is for buy offers.
To deal with expiration time, just store a tuple of (price, expiration_timestamp), compare current timestamp with the timestamp in the entry, when doing the transaction,
if the entry expired, just keep popping until a valid one is hit.
In Python, max heap needs to be done by multiplying -1 to the value in it with standard heapq or encapsulating the data structure within a class to hide such complexity.


"""
# sell [7,8,9]
# buy [5,4,3]
# eg: 6
import heapq
class Bookmarket(object):
    def __init__(self) -> None:
        # max heap is for buy offers
        # min heap for sell offers
        self.buy = []  # 要买书的，不愿意多花钱，所以最大值在上，要reach deal line
        self.sell = []  # 要卖书的，想多卖钱，所以最小值在上，要reach deal line

    def buy_book(self, price):
        # 如果sell pool里没有了，或者 6 小于 7时， 不能成交
        if not self.sell or price < self.sell[0]:
            # 因为buy是最大堆，所以要push负数
            heapq.heappush(self.buy, -price)
        else:
            deal = heapq.heappop(self.sell)

            return deal

    def sell_book(self, price):
        # 如果buy pool里没有，或者 6 大于 5 时， 不能成交。 注意self.buy[0]是负数
        if not self.buy or price > - self.buy[0]:
            # 因为sell是最小堆，所以要push正数
            heapq.heappush(self.sell, price)
        else:
            deal = -heapq.heappop(self.buy)

            return deal

bm = Bookmarket()
bm.buy_book(5)
bm.buy_book(4)
bm.buy_book(3)
bm.sell_book(7)
bm.sell_book(8)
bm.sell_book(9)
# print(bm.buy)
# print(bm.sell)
bm.buy_book(10)
# print(bm.buy)
# print(bm.sell)
bm.sell_book(4)
# print(bm.buy)
# print(bm.sell)



