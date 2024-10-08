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

        for person in range(1, n+1):
            if trust_count[person] == 0 and trusted_by[person] == n - 1:
                return person

        return -1
