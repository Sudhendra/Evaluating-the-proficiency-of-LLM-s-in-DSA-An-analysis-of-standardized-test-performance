class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parents[root_x] = root_y
                size[root_y] += size[root_x]

        def prime_factors(n):
            factors = set()
            while n % 2 == 0:
                factors.add(2)
                n //= 2
            for i in range(3, int(n**0.5)+1, 2):
                while n % i == 0:
                    factors.add(i)
                    n //= i
            if n > 2:
                factors.add(n)
            return factors

        nums_set = set(nums)
        max_num = max(nums)
        parents = list(range(max_num + 1))
        size = [1] * (max_num + 1)

        for num in nums:
            for factor in prime_factors(num):
                union(num, factor)

        components = {}
        for num in nums:
            root = find(num)
            components.setdefault(root, set()).add(num)

        return max(len(component) for component in components.values())