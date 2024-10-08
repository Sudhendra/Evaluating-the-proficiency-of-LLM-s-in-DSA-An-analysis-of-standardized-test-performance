from heapq import heappush, heappop

class Solution:
    
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglies = [1]
        heap = [(p, 0, p) for p in primes]
        
        for _ in range(1, n):
            ugly = uglies[-1]
            while heap[0][2] == ugly:
                p, i, val = heappop(heap)
                heappush(heap, (p * uglies[i], i+1, p * uglies[i]))
            uglies.append(heap[0][2])
        
        return uglies[-1]
