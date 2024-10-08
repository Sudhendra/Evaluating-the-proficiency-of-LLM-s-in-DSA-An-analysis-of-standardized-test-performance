class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        super_ugly = [1]  # Initialize with the first super ugly number
        pointers = [0] * len(primes)  # Pointers to track indices for each prime factor

        for _ in range(1, n):
            next_ugly = min([super_ugly[pointers[i]] * primes[i] for i in range(len(primes))])
            super_ugly.append(next_ugly)

            for i in range(len(primes)):
                if next_ugly == super_ugly[pointers[i]] * primes[i]:
                    pointers[i] += 1

        return super_ugly[-1]
