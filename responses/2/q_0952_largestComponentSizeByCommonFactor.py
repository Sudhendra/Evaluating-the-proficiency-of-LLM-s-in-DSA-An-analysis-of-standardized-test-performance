from typing import List

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

        def prime_factors(num):
            factors = set()
            while num % 2 == 0:
                factors.add(2)
                num //= 2
            for i in range(3, int(num**0.5) + 1, 2):
                while num % i == 0:
                    factors.add(i)
                    num //= i
            if num > 2:
                factors.add(num)
            return factors

        parent = {num: num for num in nums}
        size = {num: 1 for num in nums}

        for num in nums:
            for factor in prime_factors(num):
                if factor in parent:
                    union(num, factor)

        return max(size.values())
