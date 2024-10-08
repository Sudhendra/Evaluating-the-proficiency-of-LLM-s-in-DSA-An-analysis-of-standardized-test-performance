class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if a == b:
            return 'ab' * a
        if a > b:
            return 'aab' + self.strWithout3a3b(a - 2, b - 1) if a - b > 1 else 'ab' * a
        return 'bba' + self.strWithout3a3b(a - 1, b - 2) if b - a > 1 else 'ab' * b
