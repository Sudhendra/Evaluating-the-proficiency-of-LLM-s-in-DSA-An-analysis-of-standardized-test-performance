class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        
        def is_valid(num1, num2, start):
            if start == len(num):
                return True
            
            sum_num = str(int(num1) + int(num2))
            if not num.startswith(sum_num, start):
                return False
            
            return is_valid(num2, sum_num, start + len(sum_num))
        
        for i in range(1, len(num) // 2 + 1):
            for j in range(1, (len(num) - i) // 2 + 1):
                num1 = num[:i]
                num2 = num[i:i+j]
                
                if (len(num1) > 1 and num1.startswith('0')) or (len(num2) > 1 and num2.startswith('0')):
                    continue
                
                if is_valid(num1, num2, i + j):
                    return True
        
        return False
