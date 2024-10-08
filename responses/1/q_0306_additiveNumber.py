class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def is_valid_sequence(num, first, second):
            if not num:
                return True
            total = str(int(first) + int(second))
            if not num.startswith(total):
                return False
            return is_valid_sequence(num[len(total):], second, total)

        n = len(num)
        for i in range(1, n // 2 + 1):
            for j in range(1, n // 2 + 1):
                if num[0] == '0' and i > 1:
                    continue
                if num[i] == '0' and j > 1:
                    continue
                first = num[:i]
                second = num[i:i+j]
                if is_valid_sequence(num[i+j:], first, second):
                    return True
        return False
