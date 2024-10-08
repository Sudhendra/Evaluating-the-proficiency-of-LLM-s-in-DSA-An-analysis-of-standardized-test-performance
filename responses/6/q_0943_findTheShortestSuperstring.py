from itertools import permutations

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        def overlap(a, b):
            for i in range(len(a), 0, -1):
                if b.startswith(a[i:]):
                    return i
            return 0

        n = len(words)
        dp = [[0] * n for _ in range(1 << n)]
        path = [[0] * n for _ in range(1 << n)]

        for mask in range(1, 1 << n):
            for bit in range(n):
                if (mask >> bit) & 1:
                    prev_mask = mask ^ (1 << bit)
                    for prev_bit in range(n):
                        if dp[prev_mask][prev_bit] + overlap(words[prev_bit], words[bit]) > dp[mask][bit]:
                            dp[mask][bit] = dp[prev_mask][prev_bit] + overlap(words[prev_bit], words[bit])
                            path[mask][bit] = prev_bit

        end, last = max([(dp[-1][i], i) for i in range(n)])
        res = [last]
        mask = (1 << n) - 1

        while len(res) < n:
            prev = path[mask][last]
            res.append(prev)
            mask ^= 1 << last
            last = prev

        superstring = words[res[-1]]
        for i in range(n - 2, -1, -1):
            superstring += words[res[i]][overlap(words[res[i]], words[res[i + 1]]):]

        return superstring

