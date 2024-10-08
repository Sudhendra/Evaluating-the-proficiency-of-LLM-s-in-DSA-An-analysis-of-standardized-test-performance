from typing import List

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

        def factors(num):
            result = set()
            factor = 2
            while factor * factor <= num:
                if num % factor == 0:
                    result.add(factor)
                    num //= factor
                else:
                    factor += 1
            if num > 1:
                result.add(num)
            return result

        max_num = max(nums)
        parents = list(range(max_num + 1))
        size = [1] * (max_num + 1)

        num_to_idx = {}
        for idx, num in enumerate(nums):
            num_to_idx[num] = idx

        for num in nums:
            for factor in factors(num):
                if factor in num_to_idx:
                    union(num_to_idx[num], num_to_idx[factor])

        return max(size)

nums = [4, 6, 15, 35]
sol = Solution()
print(sol.largestComponentSize(nums))
