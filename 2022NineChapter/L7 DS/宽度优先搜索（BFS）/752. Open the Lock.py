# 题意：开锁，类似于word ladder，在deadends的不可取
# 思路：从start开始，从8个方向BFS，不在visited和deadends的入queue；
# 用ch1 = (int(ch) + 1) % 10，ch2 = (int(ch) - 1) % 10 取上下
# Time Complexity: O(N**2 A**N + D)  n是sting长度， A是10进制， D is the size of deadends
# Space Complexity: O(A**N + D) queue和set deadends

# 最多需要在队列中存储 O(A**n *n), A**n 个长度为 n 的字符串. 10 ** 4 * 4
import collections


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        start = '0000'
        deadends = set(deadends)

        if start in deadends:
            return -1

        visited = set()
        distance = 0
        q = collections.deque([start])
        while q:
            distance += 1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return distance - 1
                visited.add(cur)
                for next_number in self.get_next_numbers(cur):
                    if next_number not in deadends and next_number not in visited:
                        q.append(next_number)
                        visited.add(next_number)

        return -1

    def get_next_numbers(self, string):
        res = []
        for i in range(4):
            ch = string[i]
            ch1 = (int(ch) + 1) % 10
            ch2 = (int(ch) - 1) % 10

            next_string1 = string[:i] + str(ch1) + string[i + 1:]
            next_string2 = string[:i] + str(ch2) + string[i + 1:]
            res.append(next_string1)
            res.append(next_string2)

        return res


