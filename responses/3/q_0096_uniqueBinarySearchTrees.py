class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        catalan_number = 1
        for i in range(0, n):
            catalan_number *= 2 * (2 * i + 1) / (i + 2)
        
        return int(catalan_number)