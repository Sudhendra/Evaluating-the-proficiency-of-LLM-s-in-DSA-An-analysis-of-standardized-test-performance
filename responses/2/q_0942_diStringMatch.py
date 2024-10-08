from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        res = []
        low, high = 0, n
        
        for char in s:
            if char == 'I':
                res.append(low)
                low += 1
            else:
                res.append(high)
                high -= 1
                
        res.append(low)  # or high, no difference since we are just alternating
        
        return res