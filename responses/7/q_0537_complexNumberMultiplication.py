class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse_complex(num: str):
            real, imaginary = map(int, num[:-1].split("+"))
            return (real, imaginary)
        
        def multiply_complex(num1: tuple, num2: tuple):
            real1, imaginary1 = num1
            real2, imaginary2 = num2
            real = real1 * real2 - imaginary1 * imaginary2
            imaginary = real1 * imaginary2 + real2 * imaginary1
            return real, imaginary
        
        num1_real, num1_imaginary = parse_complex(num1)
        num2_real, num2_imaginary = parse_complex(num2)
        
        result_real, result_imaginary = multiply_complex((num1_real, num1_imaginary), (num2_real, num2_imaginary))
        
        return str(result_real) + "+" + str(result_imaginary) + "i"
