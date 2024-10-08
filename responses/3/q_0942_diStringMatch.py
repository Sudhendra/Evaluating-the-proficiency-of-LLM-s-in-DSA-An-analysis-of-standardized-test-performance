from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        left, right = 0, n
        result = []
        for char in s:
            if char == 'I':
                result.append(left)
                left += 1
            elif char == 'D':
                result.append(right)
                right -= 1
        result.append(left)
        return result