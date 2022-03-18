class Solution:
    def addBinary(self, a: str, b: str) -> str:

        indexa = len(a) - 1
        indexb = len(b) - 1
        carry = 0
        res = ""

        while indexa >= 0 or indexb >= 0 or carry:
            x = int(a[indexa]) if indexa >= 0 else 0
            y = int(b[indexb]) if indexb >= 0 else 0

            res = str((x + y + carry) % 2) + res
            carry = (x + y + carry) // 2

            indexa, indexb = indexa - 1, indexb - 1

        return res


'''
def addBinary(self, a, b):
    i, j, carry, res = len(a)-1, len(b)-1, 0, ""
    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1
        res = str(carry%2) + res
        carry //= 2
    return res
'''
'''
    def addBinary(self, a, b):
        
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        res = ""


        while i >=0 or j >=0  or carry:
            if i >=0:
                carry += int(a[i])
           
            if j >=0:
                carry += int(b[j])
          
            res = str(carry % 2) + res
            carry = carry // 2

            i -= 1
            j -= 1

        return res
'''