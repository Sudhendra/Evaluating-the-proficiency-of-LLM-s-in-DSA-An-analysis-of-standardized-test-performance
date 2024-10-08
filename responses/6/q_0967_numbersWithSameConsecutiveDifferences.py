from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def dfs(num, n):
            if n == 0:
                return [num]
            tail_digit = num % 10
            result = []
            next_digits = set([tail_digit + k, tail_digit - k])
            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    new_num = num * 10 + next_digit
                    result += dfs(new_num, n - 1)
            return result

        if n == 1:
            return [i for i in range(10)]
        
        result = []
        for i in range(1, 10):  # Avoid leading zeros
            result += dfs(i, n - 1)
        
        return result
