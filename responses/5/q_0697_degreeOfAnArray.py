from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        count = defaultdict(int)
        first_occurrence = {}
        degree = 0
        result = float('inf')
        
        for i, num in enumerate(nums):
            if num not in first_occurrence:
                first_occurrence[num] = i
            count[num] += 1
            degree = max(degree, count[num])
        
        for num in count:
            if count[num] == degree:
                result = min(result, i - first_occurrence[num] + 1)
        
        return result
