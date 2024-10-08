class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        def divide_and_conquer(n):
            if n == 1:
                return [1]
            
            odds = divide_and_conquer((n+1)//2)
            evens = divide_and_conquer(n//2)
            
            return [2*x - 1 for x in odds] + [2*x for x in evens]
        
        return divide_and_conquer(n)
