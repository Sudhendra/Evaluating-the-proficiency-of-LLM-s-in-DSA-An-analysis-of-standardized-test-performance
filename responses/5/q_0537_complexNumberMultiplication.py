class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse_complex(num):
            real, imag = map(int, num[:-1].split('+'))
            return real, imag
        
        real1, imag1 = parse_complex(num1)
        real2, imag2 = parse_complex(num2)
        
        real = real1 * real2 - imag1 * imag2
        imag = real1 * imag2 + real2 * imag1
        
        return f"{real}+{imag}i"