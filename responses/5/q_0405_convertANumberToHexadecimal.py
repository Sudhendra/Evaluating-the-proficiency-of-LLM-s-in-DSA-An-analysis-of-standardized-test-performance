class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        result = ""
        mask = 0xf
        if num < 0:
            num += 2**32

        while num > 0:
            result = hex_chars[num & mask] + result
            num >>= 4

        return result