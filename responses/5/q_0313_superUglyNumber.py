from heapq import heappush, heappop

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        super_ugly = [1]
        heap = [(p, 0, p) for p in primes]
        
        while len(super_ugly) < n:
            num, idx, prime = heappop(heap)
            if num > super_ugly[-1]:
                super_ugly.append(num)
            heappush(heap, (super_ugly[idx] * prime, idx + 1, prime))
        
        return super_ugly[-1]
