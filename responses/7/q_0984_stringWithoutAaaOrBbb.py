class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if a > b:
            return self.helper(a, b, 'a', 'b')
        else:
            return self.helper(b, a, 'b', 'a')

    def helper(self, a, b, bigger, smaller):
        result = ''
        while a > 0 or b > 0:
            if a > 0:
                result += bigger
                a -= 1
            if a > b:
                result += bigger
                a -= 1
            if b > 0:
                result += smaller
                b -= 1
        return result