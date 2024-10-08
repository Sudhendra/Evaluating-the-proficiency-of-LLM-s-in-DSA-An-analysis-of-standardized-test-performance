from typing import List

class Solution:

    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        res = list(range(n+1))
        low, high = 0, n
        
        output = []
        for char in s:
            if char == 'I':
                output.append(res[low])
                low += 1
            else:
                output.append(res[high])
                high -= 1
        
        output.append(res[low])  # Append the last remaining number
        
        return output
