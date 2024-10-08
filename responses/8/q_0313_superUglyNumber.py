class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglies = [1]
        pointers = [0] * len(primes)
        
        for _ in range(1, n):
            candidates = [uglies[pointers[i]] * primes[i] for i in range(len(primes))]
            min_val = min(candidates)
            uglies.append(min_val)
            
            for i in range(len(pointers)):
                if candidates[i] == min_val:
                    pointers[i] += 1
        
        return uglies[-1]
