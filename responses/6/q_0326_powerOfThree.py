class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        max_power_of_three = 3 ** int((log(2**31) / log(3)))
        return max_power_of_three % n == 0
