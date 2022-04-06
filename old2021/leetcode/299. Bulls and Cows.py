class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        A = 0
        B = 0
        dic_a = {}
        dic_b = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:

                if secret[i] not in dic_a:
                    dic_a[secret[i]] = 1
                else:
                    dic_a[secret[i]] += 1

                if guess[i] not in dic_b:
                    dic_b[guess[i]] = 1
                else:
                    dic_b[guess[i]] += 1

        for k in dic_a:
            if k in dic_b:
                B = B + min(dic_a[k], dic_b[k])

        return str(A) + 'A' + str(B) + 'B'