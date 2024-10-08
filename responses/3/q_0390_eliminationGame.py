class Solution:
    def lastRemaining(self, n: int) -> int:
        remaining = n
        head = 1
        step = 1
        from_left = True

        while remaining > 1:
            if from_left or remaining % 2 == 1:
                head += step

            remaining //= 2
            step *= 2
            from_left = not from_left

        return head