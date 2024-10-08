from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        perm = list(range(n+1))
        result = []

        low, high = 0, n
        for char in s:
            if char == 'I':
                result.append(perm[low])
                low += 1
            else:
                result.append(perm[high])
                high -= 1

        result.append(perm[low])

        return result