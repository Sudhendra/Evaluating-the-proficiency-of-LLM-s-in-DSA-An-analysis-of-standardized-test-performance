class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def is_valid(num1, num2, remaining):
            if not remaining:
                return True
            sum_str = str(int(num1) + int(num2))
            if remaining.startswith(sum_str):
                return is_valid(num2, sum_str, remaining[len(sum_str):])
            return False

        n = len(num)
        for i in range(1, n // 2 + 1):
            for j in range(i + 1, n):
                if (num[0] == '0' and i > 1) or (num[i] == '0' and j > i + 1):
                    continue
                num1 = num[:i]
                num2 = num[i:j]
                if is_valid(num1, num2, num[j:]):
                    return True
        return False
