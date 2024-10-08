from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]

        res = []

        def dfs(curr_num, level):
            if level == n:
                res.append(curr_num)
                return

            last_digit = curr_num % 10

            for next_digit in {last_digit + k, last_digit - k}:
                if 0 <= next_digit <= 9:
                    new_num = curr_num * 10 + next_digit
                    dfs(new_num, level + 1)

        for i in range(1, 10):
            dfs(i, 1)

        return res