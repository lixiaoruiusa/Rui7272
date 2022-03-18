class Solution:
    def addBinary(self, a: str, b: str) -> str:

        a = list(a)
        b = list(b)
        res = ''
        carry = 0

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            res = str(carry % 2) + res
            carry = carry // 2
        return res

    
'''
class Solution:
    """
    @param a: a number
    @param b: a number
    @return: the result
    @ Time ： O(n)  Space：O(n)
    @判断每一位方法：(x+y+carry) % 2 == 0
    @计算carry方法：(x+y+carry) // 2
    """
    def addBinary(self, a, b):
        #conor case
        if a == '':
            return b
        if b == '':
            return a
        idx_a = len(a) - 1
        idx_b = len(b) - 1
        carry = 0
        sum = ''
        while idx_a >= 0 or idx_b >=0:
            x = int(a[idx_a]) if idx_a >= 0 else 0
            y = int(b[idx_b]) if idx_b >= 0 else 0
            if (x+y+carry) % 2 == 0:
                sum = '0' + sum
            else:
                sum = '1' + sum
            carry = (x + y + carry) // 2
            idx_a -= 1
            idx_b -= 1
        if carry == 1:
            sum = '1' + sum
        return sum


'''