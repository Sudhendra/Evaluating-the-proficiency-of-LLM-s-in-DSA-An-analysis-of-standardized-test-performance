from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_count = Counter(nums)
        result = 0
        for num in num_count:
            if num + 1 in num_count:
                result = max(result, num_count[num] + num_count[num + 1])
        return result
