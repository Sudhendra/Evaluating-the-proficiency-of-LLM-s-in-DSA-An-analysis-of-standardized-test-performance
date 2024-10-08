class Solution:
    """Given an integer `n`, return *the number of trailing zeroes in* `n!`.

    Note that `n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1`.
    """

    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count
