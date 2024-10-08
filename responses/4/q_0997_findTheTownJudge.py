from collections import Counter

class Solution:
    def findJudge(self, n: int, trust: List[List[int]) -> int:
        if n == 1 and not trust:
            return 1
        
        trusted_count = Counter()
        trusted_by_count = Counter()

        for a, b in trust:
            trusted_by_count[a] += 1
            trusted_count[b] += 1

        for person in range(1, n+1):
            if trusted_count[person] == n - 1 and trusted_by_count[person] == 0:
                return person
        
        return -1
