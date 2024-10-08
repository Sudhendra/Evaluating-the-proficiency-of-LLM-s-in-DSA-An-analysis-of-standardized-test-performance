from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
        
        in_degrees = [0] * (n + 1)
        out_degrees = [0] * (n + 1)
        
        for a, b in trust:
            out_degrees[a] += 1
            in_degrees[b] += 1
        
        for i in range(1, n+1):
            if in_degrees[i] == n-1 and out_degrees[i] == 0:
                return i
        
        return -1
