# O(N * K) time and # O(N) space n is height, k is allowed steps
def staircaseTraversal(height, maxSteps):
    dp = [0] * (height + 1)
    dp[0] = 1

    for i in range(1, maxSteps + 1):
        dp[i] = sum(dp)

    for j in range(maxSteps + 1, height + 1):
        dp[j] = sum(dp[j - maxSteps: j])

    return dp[-1]


# O(N) time and space n is height

def staircaseTraversal(height, maxSteps):
    dp = [1]
    currentNumWays = 0
    for current in range(1, height + 1):
        startIdx = current - maxSteps - 1
        endIdx = current - 1

        if startIdx >= 0:
            currentNumWays -= dp[startIdx]
        currentNumWays += dp[endIdx]
        dp.append(currentNumWays)

    return dp[-1]
