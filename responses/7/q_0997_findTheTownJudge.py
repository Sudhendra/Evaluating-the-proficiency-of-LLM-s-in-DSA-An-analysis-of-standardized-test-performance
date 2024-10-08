from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1
        
        trustees = defaultdict(set)
        trusted_by = defaultdict(int)
        
        for a, b in trust:
            trustees[a].add(b)
            trusted_by[b] += 1
        
        for i in range(1, n+1):
            if not trustees[i] and trusted_by[i] == n-1:
                return i
        
        return -1
