from typing import List

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = [i+1 for i in range(n)]
        for i in range(1, k):
            ans[i:] = ans[:i-1:-1]  # Reverse elements after i-1
        return ans
