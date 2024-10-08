class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def is_valid(num1, num2, rest):
            if not rest:
                return True
            num3 = str(int(num1) + int(num2))
            if rest.startswith(num3):
                return is_valid(num2, num3, rest[len(num3):])
            return False
        
        n = len(num)
        for i in range(1, n // 2 + 1):
            for j in range(1, n // 2 + 1):
                if max(i, j) > 1 and num[0] == '0' or num[i] == '0' and j > 1:
                    continue
                if is_valid(num[:i], num[i:i+j], num[i+j:]):
                    return True
        return False
