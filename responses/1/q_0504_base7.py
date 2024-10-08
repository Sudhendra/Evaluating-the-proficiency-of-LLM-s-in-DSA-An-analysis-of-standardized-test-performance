class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        result = ""
        is_negative = False
        if num < 0:
            is_negative = True
            num = abs(num)

        while num > 0:
            remainder = num % 7
            result = str(remainder) + result
            num //= 7

        if is_negative:
            result = "-" + result

        return result