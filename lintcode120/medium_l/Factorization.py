import math
class Solution:
    """
    @param n: An integer
    @return: a list of combination
    @ 时间复杂度O(nlog(n)) dfs搜索
    @空间复杂度O(n) 记录所有因子组合
    """

    def getFactors(self, n):
        # write your code here
        result = []
        self.dfs(result, [], 2, n)
        print('final',result)
        return result

    def dfs(self, result, path, lastF, reminder):
        print('调用dfs')
        print('reminder', reminder)
        if path:
            path.append(reminder)
            result.append(path[:])
            path.pop()

        for i in range(lastF, int(math.sqrt(reminder) + 1)):
            if reminder % i != 0: continue
            path.append(i)
            self.dfs(result, path, i, reminder // i)
            path.pop()

        print('结束调用dfs')
        # print('result',result)
        # print('path', path)
        # print('lastF', lastF)
        # print('reminder', reminder)

w1 = Solution()
w1.getFactors(6)