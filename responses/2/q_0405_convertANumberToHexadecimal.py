class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        elif num < 0:
            num += 2**32
        hex_chars = "0123456789abcdef"
        result = ""
        while num:
            result = hex_chars[num % 16] + result
            num //= 16
        return result
