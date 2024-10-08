from collections import Counter

class Solution:

    def reorderedPowerOf2(self, N: int) -> bool:
        
        def digits_count(num):
            return Counter(str(num))
        
        count_n = digits_count(N)
        
        for i in range(30):
            if count_n == digits_count(1 << i):
                return True
            
        return False
