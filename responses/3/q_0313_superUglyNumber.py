class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        super_ugly = [1]
        pointers = [0] * len(primes)
        
        while len(super_ugly) < n:
            candidates = [prime * super_ugly[pointers[i]] for i, prime in enumerate(primes)]
            next_ugly = min(candidates)
            
            for i, candidate in enumerate(candidates):
                if candidate == next_ugly:
                    pointers[i] += 1
        
            if next_ugly != super_ugly[-1]:
                super_ugly.append(next_ugly)
        
        return super_ugly[-1]