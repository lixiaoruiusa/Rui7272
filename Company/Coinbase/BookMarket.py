"""
请问楼主关于 buy and sell textbooks 那道题 的input和output到底是什么啊？
我的理解是这个market place 只有两个api ---> sell 和 buy
大概就是这样一个object

然后人们只能interact with sell and buy function. 所以每个order是individually added.
"""

"""
之前刷面经以为妥妥的是 in memory file system
结果出了 买卖书籍的题
有点像股市的order book, 首先有一些 buy order， 再有一些 sell order
这些order 不会匹配
自己写个method去买/卖书，在提供一个你期望的价格
我写的大概就是tradeBook(isBuy, price) 这样的一个method
如果能匹配就提供order book里面最好的价格（buy就是最低的，sell就是最高的），不match 就加到order book里面
我用的min max heap分别写了buyOrderbook 和 sellOrderBook

Follow up 1：我这个method地方有什么不OK的地方
一开始想了半天也没想出来..觉得bug free
后来我发现没有handle order book空了的情况，但面试官显然找的不是这个
后来又谈到price上的问题，我才反应过来 price不能为负值。
Follow up 2: 这些offer 会expire
我就自己建了一个custom class 里面有一个expireDate
在call我的method的时候，遇见expire的就poll掉，直到找到不expire的match..
面试官也同意了，其实没完全写完就叫停了‍‍‌‍‌‌‍‍‌‍‌‍‌‌‍‍‍‌‌‍。紧接着问了问time complexity啥的

"""
import heapq
class BookMarket(object):
    def __init__(self) -> None:
        self.buys = []
        self.sells = []


    def buy(self, price):
        pass


    def sell(self, price):
        pass