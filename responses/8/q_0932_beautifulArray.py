from typing import List

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        def divide_and_conquer(arr):
            if len(arr) <= 1:
                return arr
            odds = divide_and_conquer([x * 2 - 1 for x in arr if x * 2 - 1 <= n // 2])
            evens = divide_and_conquer([x * 2 for x in arr if x * 2 <= n // 2])
            return odds + evens
        
        return divide_and_conquer(range(1, n + 1))
