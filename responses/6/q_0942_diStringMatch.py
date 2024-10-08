from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        low, high = 0, n
        result = []
        
        for char in s:
            if char == 'I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        
        result.append(low)  # or high, as both will be the same value
        
        return result
