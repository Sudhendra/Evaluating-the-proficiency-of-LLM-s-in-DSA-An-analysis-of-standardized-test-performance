class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse_complex_number(num):
            real, imag = map(int, num[:-1].split('+'))
            return real, imag

        a, b = parse_complex_number(num1)
        c, d = parse_complex_number(num2)

        real = a * c - b * d
        imag = a * d + b * c

        return f"{real}+{imag}i"
