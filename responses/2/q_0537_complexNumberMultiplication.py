class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1_real, num1_imaginary = map(int, num1[:-1].split('+'))
        num2_real, num2_imaginary = map(int, num2[:-1].split('+')

        result_real = num1_real * num2_real - num1_imaginary * num2_imaginary
        result_imaginary = num1_real * num2_imaginary + num1_imaginary * num2_real

        return f"{result_real}+{result_imaginary}i"
