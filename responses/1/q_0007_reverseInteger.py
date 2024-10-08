class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1

        reversed_num = 0
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        reversed_num *= sign

        if reversed_num < -(2**31) or reversed_num > 2**31 - 1:
            return 0

        return reversed_num