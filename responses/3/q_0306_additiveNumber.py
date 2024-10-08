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
        for i in range(1, n):
            for j in range(i+1, n):
                num1, num2 = num[:i], num[i:j]
                if (len(num1) > 1 and num1.startswith('0')) or (len(num2) > 1 and num2.startswith('0')):
                    continue
                if is_valid(num1, num2, num[j:]):
                    return True
        return False
