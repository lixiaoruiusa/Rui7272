# O(n) time | O(n) space

def minRewards(scores):
    # Write your code here.
    dp = [1] * len(scores)

    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            dp[i] = dp[i - 1] + 1

    for j in reversed(range(len(scores) - 1)):
        if scores[j + 1] < scores[j]:
            dp[j] = max(dp[j], dp[j + 1] + 1)

    return sum(dp)
