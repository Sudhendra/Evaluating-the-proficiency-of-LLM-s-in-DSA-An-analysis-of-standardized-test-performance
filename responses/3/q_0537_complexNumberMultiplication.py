class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        p1, q1 = map(int, num1[:-1].split('+'))
        p2, q2 = map(int, num2[:-1].split('+'))
        return f"{p1*p2 - q1*q2}+{p1*q2 + p2*q1}i"