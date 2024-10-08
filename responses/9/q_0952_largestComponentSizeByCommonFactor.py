from typing import List

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parents[root_x] = root_y
                sizes[root_y] += sizes[root_x]
        
        def get_factors(num):
            factors = set()
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    factors.add(i)
                    factors.add(num // i)
            return factors
        
        max_num = max(nums)
        parents = list(range(max_num + 1))
        sizes = [1] * (max_num + 1)
        
        factors_to_num = {}
        for num in nums:
            for factor in get_factors(num):
                if factor in factors_to_num:
                    union(num, factors_to_num[factor])
                factors_to_num[factor] = find(num)
        
        return max(sizes)

# Test the solution with the examples provided
solution = Solution()
print(solution.largestComponentSize([4, 6, 15, 35]))  # Output: 4
print(solution.largestComponentSize([20, 50, 9, 63]))  # Output: 2
print(solution.largestComponentSize([2, 3, 6, 7, 4, 12, 21, 39]))  # Output: 8
