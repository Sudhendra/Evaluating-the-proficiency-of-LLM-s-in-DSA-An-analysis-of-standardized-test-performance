class Solution:
    
    def lastRemaining(self, n: int) -> int:
        remaining = n
        start = 1
        step = 1
        left_to_right = True
        
        while remaining > 1:
            if left_to_right or remaining % 2 == 1:
                start += step
            remaining //= 2
            step *= 2
            left_to_right = not left_to_right
        
        return start
