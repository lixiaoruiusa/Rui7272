class Solution:
    def expand(self, s: str) -> List[str]:
        candidates = []
        p = 0
        while p < len(s):
            tmp = []
            if s[p] == "{":
                p += 1
                while s[p] != "}":
                    if s[p] != ',':
                        tmp.append(s[p])
                    p += 1
            else:
                tmp.append(s[p])
            candidates.append(tmp)
            p += 1

        # print(candidates)
        # candidates = [['a', 'b'], ['c'], ['d', 'e'], ['f']]

        n = len(candidates)
        ans = []

        def helper(path, idx):
            if idx == n:
                ans.append("".join(path[:]))
                return

            letters = candidates[idx]
            for l in letters:
                path.append(l)
                helper(path, idx + 1)
                path.pop()

        helper([], 0)

        """

        n = len(candidates)
        q = collections.deque([])
        ans = []
        for c in candidates[0]:
            q.append((c, 0))

       # q is ('a', 0) ('b', 0)

        while q:
            path, idx = q.popleft()
            if idx == n - 1:
                ans.append(path)
                continue

            for c in candidates[idx+1]:
                new_str = path[:] + c
                q.append((new_str, idx+1))

        """

        return sorted(ans) 