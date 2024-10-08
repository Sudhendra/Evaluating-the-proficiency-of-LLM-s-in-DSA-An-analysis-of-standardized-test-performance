from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = Counter(nums)
        result = 0
        for num in counts:
            if num + 1 in counts:
                result = max(result, counts[num] + counts[num + 1])
        return result
