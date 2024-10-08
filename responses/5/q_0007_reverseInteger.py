class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        is_negative = x < 0
        x = abs(x)

        reversed_x = 0
        while x != 0:
            digit = x % 10
            x //= 10

            if is_negative:
                if reversed_x > 214748364 or (reversed_x == 214748364 and digit > 8):
                    return 0
                reversed_x = reversed_x * 10 + digit
            else:
                if reversed_x > 214748364 or (reversed_x == 214748364 and digit > 7):
                    return 0
                reversed_x = reversed_x * 10 + digit

        return -reversed_x if is_negative else reversed_x
