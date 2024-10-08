from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]) -> int:
        if len(trust) < n - 1:
            return -1

        trust_count = defaultdict(int)
        trusted_by = defaultdict(int)

        for a, b in trust:
            trust_count[a] -= 1
            trusted_by[b] += 1

        for i in range(1, n + 1):
            if trust_count[i] == -(n - 1) and trusted_by[i] == n - 1:
                return i

        return -1
