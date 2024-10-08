class Solution:
    
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:  # If k is divisible by 2 or 5, n will never be divisible by k
            return -1
        
        remainder = 0
        for length_n in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:  # Found the smallest n that is divisible by k
                return length_n

        return -1
