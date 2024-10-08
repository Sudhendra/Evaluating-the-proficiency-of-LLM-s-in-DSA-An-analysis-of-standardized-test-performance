class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 1:
            return False
        x = num
        while x*x > num:
            x = (x + num//x) // 2
        return x*x == num