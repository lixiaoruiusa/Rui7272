'''
Alice and Bob work in a beautiful orchard. There are N  apple trees in the orchard. The apple trees are arranged in a row and they are numbered from 1 to N. Alice is planning to collect all the apples from K consecutive trees and Bob is planning to collect all the apples from L consecutive trees. They want to choose two disjoint segments (one consisting of K trees for Alice and the other consisting of L trees for Bob) so as not to disturb each other. What is the maximum number of apples that they can collect? Write a function that, given an array A consisting of N integers denoting the number of apples on each apple tree in the row, and integers K and L denoting, respectively, the number of trees that Alice and Bob can choose when collecting, returns the maximum number of apples that can be collected by them, or −1 if there are no such intervals. For example, given A = [6, 1, 4, 6, 3, 2, 7, 4], K = 3, L = 2, your function should return 24, because Alice can choose trees 3 to 5 and collect 4 + 6 + 3 = 13 apples, and Bob can choose trees 7 to 8 and collect 7 + 4 = 11 apples. Thus, they will collect 13 + 11 = 24 apples in total, and that is the maximum number that can be achieved. Given A = [10, 19, 15], K = 2, L = 2, your function should return −1, because it is not possible for Alice and Bob to choose two disjoint intervals.
'''


def solution(A, K, L):
    if K + L > len(A):
        return -1
    for i in range(1,len(A)):
        A[i] += A[i-1]
    res = A[K+L-1]
    Kmax = A[K-1]
    Lmax = A[L-1]
    
    for i in range(K+L,len(A)):
        Kmax = max(Kmax, A[i-L] - A[i-L-K])
        Lmax = max(Lmax, A[i-K] - A[i-L-K])
        res = max(res, Kmax + A[i] - A[i-L], Lmax + A[i] - A[i-K])
    return res
