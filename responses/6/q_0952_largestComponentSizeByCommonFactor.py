class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_x] = root_y
                size[root_y] += size[root_x]

        def sieve_of_eratosthenes(n):
            primes = []
            is_prime = [True] * (n+1)
            for p in range(2, n+1):
                if is_prime[p]:
                    primes.append(p)
                    for i in range(p*p, n+1, p):
                        is_prime[i] = False
            return primes

        max_num = max(nums)
        parent = list(range(max_num + 1))
        size = [1] * (max_num + 1)

        primes = sieve_of_eratosthenes(max_num)
        
        num_map = {}
        for i, num in enumerate(nums):
            num_map[num] = i

        for num in nums:
            for p in primes:
                if p > num:
                    break
                if num % p == 0 and p in num_map:
                    union(num_map[num], num_map[p])

        return max(size)
