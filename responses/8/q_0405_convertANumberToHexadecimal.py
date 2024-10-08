class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return "0"
        hex_chars = "0123456789abcdef"
        result = ""
        mask = 0xf
        while num != 0:
            result = hex_chars[num & mask] + result
            num = (num >> 4) & 0xffffffff
        return result
