from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtrack(path, n, k):
            if len(path) == n:
                num = int(''.join(path))
                if len(str(num)) == n:
                    result.append(num)
                return
            if not path:
                for i in range(1, 10):
                    backtrack(path + [str(i)], n, k)
            else:
                last_digit = int(path[-1])
                for next_digit in {last_digit - k, last_digit + k}:
                    if 0 <= next_digit <= 9:
                        backtrack(path + [str(next_digit)], n, k)

        result = []
        backtrack([], n, k)
        return result
