from heapq import heappush, heappop

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        heap = [(p, 1) for p in primes]
        
        for _ in range(1, n):
            num, idx = heappop(heap)
            while ugly[-1] == num:
                num, idx = heappop(heap)
            ugly.append(num)
            for i in range(idx, len(ugly)):
                heappush(heap, (ugly[i]*num, i))
        
        return ugly[-1]