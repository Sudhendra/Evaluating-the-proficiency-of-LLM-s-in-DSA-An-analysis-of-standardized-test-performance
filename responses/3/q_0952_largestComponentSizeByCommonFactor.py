from collections import defaultdict

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:

        def primes(n):
            sieve = [True] * n
            for p in range(2, int(n ** 0.5) + 1):
                if sieve[p]:
                    sieve[p * p:n:p] = [False] * len(sieve[p * p:n:p])
            return [p for p in range(2, n) if sieve[p]]

        n = len(nums)
        dsu = DSU(n)
        primes_list = primes(max(nums) + 1)
        prime_to_idx = {prime: idx for idx, prime in enumerate(primes_list)}

        for idx, num in enumerate(nums):
            for prime in primes_list:
                if prime > num:
                    break
                if num % prime == 0:
                    if prime in prime_to_idx:
                        dsu.union(idx, prime_to_idx[prime])

        count = defaultdict(int)
        for idx, num in enumerate(nums):
            count[dsu.find(idx)] += 1

        return max(count.values())
