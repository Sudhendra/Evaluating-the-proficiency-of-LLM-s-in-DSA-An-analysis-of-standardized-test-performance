from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1
            
        degree = max(count.values())
        ans = len(nums)
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)
        
        return ans
