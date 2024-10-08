from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        result = [0, 1]
        base = 2
        
        for i in range(2, n+1):
            for j in range(len(result)-1, -1, -1):
                result.append(base + result[j])
            
            base *= 2
        
        return result
