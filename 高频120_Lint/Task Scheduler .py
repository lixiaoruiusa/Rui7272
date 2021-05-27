class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """

    def leastInterval(self, tasks, n):
        # write your code here
        dic = {}
        for task in tasks:
            if task not in dic:
                dic[task] = 0
            else:
                dic[task] += 1

        longest = max(dic.values())

        ans = (longest - 1) * (n + 1)

        for times in dic.values():
            if times == longest:
                ans += 1

        return max(len(tasks), ans)