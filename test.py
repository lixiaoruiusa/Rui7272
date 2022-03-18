"""
Input
n - postitive number
p - positive prime number

Output
k - no-nagetive number

Condition
n!=(p^k)*m where m is a integer and m % p != 0

Example
n=6,p=2
n!=6*5*4*3*2*1
=(3*2)*5*(2*2)*3*2
=(2^4)*45
=((p=2)^(k=4))*(m=45)

k=4

"""


def fun1(n,p):

    count = 0
    for fact in range(1, n):
        while fact % p == 0:
            count += 1
            fact = fact / p

    return count

print(fun1(1000,2))

