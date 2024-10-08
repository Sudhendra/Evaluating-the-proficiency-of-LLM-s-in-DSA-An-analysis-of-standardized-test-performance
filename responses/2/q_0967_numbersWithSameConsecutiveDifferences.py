from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]

        ans = []

        def dfs(num: int, steps: int):
            if steps == n:
                ans.append(num)
                return

            last_digit = num % 10

            if last_digit + k < 10:
                dfs(num * 10 + last_digit + k, steps + 1)

            if k != 0 and last_digit - k >= 0:
                dfs(num * 10 + last_digit - k, steps + 1)

        for i in range(1, 10):
            dfs(i, 1)

        return ans

# Example usage
sol = Solution()
print(sol.numsSameConsecDiff(3, 7))  # Output: [181, 292, 707, 818, 929]
print(sol.numsSameConsecDiff(2, 1))  # Output: [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]
