class Solution:
    
    def isAdditiveNumber(self, num: str) -> bool:
        def is_valid(num1, num2, start):
            if start == len(num):
                return True
            num3 = str(int(num1) + int(num2))
            if num.startswith(num3, start):
                return is_valid(num2, num3, start + len(num3))
            return False
        
        for i in range(1, len(num) // 2 + 1):
            for j in range(1, (len(num) - i) // 2 + 1):
                if (i > 1 and num[0] == '0') or (j > 1 and num[i] == '0'):
                    continue
                num1, num2 = num[:i], num[i:i+j]
                if is_valid(num1, num2, i+j):
                    return True
        return False
