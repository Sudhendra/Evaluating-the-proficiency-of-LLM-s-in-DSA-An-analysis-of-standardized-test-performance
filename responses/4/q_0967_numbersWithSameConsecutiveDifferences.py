class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]

        results = []

        def dfs(num, n):
            if n == 0:
                results.append(num)
                return

            last_digit = num % 10

            if last_digit + k < 10:
                dfs(num * 10 + last_digit + k, n - 1)

            if k != 0 and last_digit - k >= 0:
                dfs(num * 10 + last_digit - k, n - 1)

        for i in range(1, 10):
            dfs(i, n - 1)

        return results
