class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        result = ""
        while a > 0 or b > 0:
            if len(result) >= 2 and result[-1] == result[-2]:
                if result[-1] == 'a':
                    result += 'b'
                    b -= 1
                else:
                    result += 'a'
                    a -= 1
            elif a >= b:
                result += 'a'
                a -= 1
            else:
                result += 'b'
                b -= 1
        return result
