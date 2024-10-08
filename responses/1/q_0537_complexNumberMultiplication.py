class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, b = map(int, num1[:-1].split('+'))
        c, d = map(int, num2[:-1].split('+'))
        real_part = a * c - b * d
        imaginary_part = a * d + b * c
        return f"{real_part}+{imaginary_part}i"