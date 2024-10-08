class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse_complex(num: str):
            real, imag = map(int, num[:-1].split('+'))
            return (real, imag)

        def format_complex(real: int, imag: int):
            return f"{real}+{imag}i"

        num1_real, num1_imag = parse_complex(num1)
        num2_real, num2_imag = parse_complex(num2)

        result_real = num1_real * num2_real - num1_imag * num2_imag
        result_imag = num1_real * num2_imag + num1_imag * num2_real

        return format_complex(result_real, result_imag)
