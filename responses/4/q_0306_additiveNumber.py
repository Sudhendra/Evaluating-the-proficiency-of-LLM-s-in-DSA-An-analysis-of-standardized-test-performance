class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def is_valid(num1, num2, start):
            if start == len(num):
                return True
            
            num_sum = str(int(num1) + int(num2))
            if num.startswith(num_sum, start):
                return is_valid(num2, num_sum, start + len(num_sum))
            return False

        if len(num) < 3:
            return False
        
        for i in range(1, len(num) // 2 + 1):
            for j in range(1, len(num) // 2 + 1):
                num1 = num[:i]
                num2 = num[i:i+j]
                
                if (len(num1) > 1 and num1.startswith('0')) or (len(num2) > 1 and num2.startswith('0')):
                    continue
                
                if is_valid(num1, num2, i + j):
                    return True
        return False
