class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(i, perm):
            nonlocal count
            if i > n:
                count += 1
                return
            for num in range(1, n+1):
                if num not in perm and (num % i == 0 or i % num == 0):
                    backtrack(i + 1, perm + [num])

        count = 0
        backtrack(1, [])
        return count
