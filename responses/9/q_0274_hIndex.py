from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        papers = [0] * (n + 1)
        
        for c in citations:
            papers[min(c, n)] += 1
        
        total = 0
        for i in range(n, -1, -1):
            total += papers[i]
            if total >= i:
                return i
        return 0
