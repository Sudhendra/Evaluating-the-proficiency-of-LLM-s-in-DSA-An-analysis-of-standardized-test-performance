class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def prime_factors(num):
            factors = set()
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    factors.add(i)
                    while num % i == 0:
                        num //= i
            if num > 1:  # Handling the case when the number itself is prime
                factors.add(num)
            return factors

        uf = UnionFind(max(nums) + 1)
        num_to_idx = {}
        for idx, num in enumerate(nums):
            num_to_idx[num] = idx
        
        for num in nums:
            factors = prime_factors(num)
            for factor in factors:
                if factor in num_to_idx:
                    uf.union(num_to_idx[num], num_to_idx[factor])
        
        count = collections.Counter(uf.find(idx) for idx in num_to_idx.values())
        
        return max(count.values())
