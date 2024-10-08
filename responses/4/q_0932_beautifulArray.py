from typing import List

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        def divide_conquer(left, right):
            if left == right:
                return [left]
            
            odd = [2*i - 1 for i in divide_conquer((left + 1) // 2, right // 2)]
            even = [2*i for i in divide_conquer(left // 2, right // 2)]
            
            return odd + even
        
        return divide_conquer(1, n+1)
