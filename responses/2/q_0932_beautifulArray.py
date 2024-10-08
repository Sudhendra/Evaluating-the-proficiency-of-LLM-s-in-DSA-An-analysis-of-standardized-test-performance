class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        if n == 1:
            return [1]

        odds = [2*i-1 for i in range(1, (n+1)//2+1)]
        evens = [2*i for i in range(1, n//2+1)]

        return self.beautifulArray(len(odds)) + self.beautifulArray(len(evens))