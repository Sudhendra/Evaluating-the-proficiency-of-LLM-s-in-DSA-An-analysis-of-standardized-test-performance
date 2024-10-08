class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1_real, num1_imag = map(int, num1[:-1].split('+'))
        num2_real, num2_imag = map(int, num2[:-1].split('+'))

        result_real = num1_real * num2_real - num1_imag * num2_imag
        result_imag = num1_real * num2_imag + num1_imag * num2_real

        return f"{result_real}+{result_imag}i"
