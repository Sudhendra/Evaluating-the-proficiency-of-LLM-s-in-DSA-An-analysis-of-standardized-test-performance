from typing import List

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        memo = {1: [1]}
        def helper(num):
            if num not in memo:
                odds = helper((num + 1) // 2)
                evens = helper(num // 2)
                memo[num] = [2*x-1 for x in odds] + [2*x for x in evens]
            return memo[num]
        
        return helper(n)
