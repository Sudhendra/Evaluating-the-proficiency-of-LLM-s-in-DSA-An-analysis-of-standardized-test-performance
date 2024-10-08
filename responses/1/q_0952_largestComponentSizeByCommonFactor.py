from typing import List

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        # Implementation of the largestComponentSize method goes here

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
                count[rootY] += count[rootX]

        limit = max(nums)
        parent = list(range(limit + 1))
        count = [1] * (limit + 1)
        primes = []

        for num in range(2, limit + 1):
            if parent[num] == num:
                for multiple in range(num * 2, limit + 1, num):
                    if parent[multiple] != multiple:
                        union(num, multiple)

        component_sizes = {}
        result = 1

        for num in nums:
            root = find(num)
            if root not in component_sizes:
                component_sizes[root] = 1
            else:
                component_sizes[root] += 1
            result = max(result, component_sizes[root])

        return result
