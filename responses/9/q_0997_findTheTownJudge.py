from collections import Counter

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return 1 if n == 1 else -1

        trusted_by = Counter()  # Count of people trusting each person
        trusts = Counter()  # Count of people each person trusts

        for a, b in trust:
            trusts[a] += 1
            trusted_by[b] += 1

        for person in range(1, n+1):
            if trusts[person] == 0 and trusted_by[person] == n - 1:
                return person

        return -1
