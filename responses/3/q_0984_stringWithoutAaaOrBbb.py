class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = ""
        while a > 0 or b > 0:
            if len(res) >= 2 and res[-1] == res[-2]:
                write_a = res[-1] == 'b'
            else:
                write_a = a >= b

            if write_a:
                res += 'a'
                a -= 1
            else:
                res += 'b'
                b -= 1

        return res