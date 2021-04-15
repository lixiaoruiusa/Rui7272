# O(nlogn) time | O(1) space
# 如果 V > c + 1 ==> c + 1 不可以， 如果 V <= C + 1, C + V都可以
def nonConstructibleChange(coins):
    if 1 not in coins:
        return 1
    coins = sorted(coins)
    change = 0
    for coin in coins:
        if coin > change + 1:
            return change + 1
        else:
            change = change + coin
    return change + 1
