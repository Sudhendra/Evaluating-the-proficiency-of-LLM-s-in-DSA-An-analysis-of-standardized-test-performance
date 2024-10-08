class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        n = abs(num)
        base_7 = ""
        while n:
            base_7 = str(n % 7) + base_7
            n //= 7

        return "-" + base_7 if num < 0 else base_7