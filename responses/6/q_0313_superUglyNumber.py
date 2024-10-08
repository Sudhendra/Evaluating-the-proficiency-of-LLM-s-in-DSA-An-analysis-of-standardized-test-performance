class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        super_ugly = [1]
        pointers = [0] * len(primes)

        for _ in range(1, n):
            candidates = [prime * super_ugly[pointers[i]] for i, prime in enumerate(primes)]
            min_val = min(candidates)
            for i in range(len(primes)):
                if candidates[i] == min_val:
                    pointers[i] += 1
            super_ugly.append(min_val)

        return super_ugly[-1]
