class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        remainders = set()
        n = 0
        length = 0
        
        while n % k != 0:
            length += 1
            n = (n * 10 + 1) % k
            
            if n in remainders:
                return -1
                
            remainders.add(n)
        
        return length
