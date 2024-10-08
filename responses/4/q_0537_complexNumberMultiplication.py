class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse_complex(s):
            real, imag = map(int, s[:-1].split('+'))
            return real, imag

        real1, imag1 = parse_complex(num1)
        real2, imag2 = parse_complex(num2)

        real_res = real1 * real2 - imag1 * imag2
        imag_res = real1 * imag2 + real2 * imag1

        return f"{real_res}+{imag_res}i"
