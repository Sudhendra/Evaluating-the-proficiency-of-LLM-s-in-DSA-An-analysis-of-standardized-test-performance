class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = []

        def backtrack(num, length):
            if length == n:
                result.append(num)
                return
            last_digit = num % 10
            if last_digit + k < 10:
                backtrack(num * 10 + last_digit + k, length + 1)
            if k != 0 and last_digit - k >= 0:
                backtrack(num * 10 + last_digit - k, length + 1)

        for i in range(1, 10):
            backtrack(i, 1)

        return result