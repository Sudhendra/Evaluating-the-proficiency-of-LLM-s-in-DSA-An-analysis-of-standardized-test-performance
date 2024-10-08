class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        result = 0
        
        for num in count:
            if num + 1 in count:
                result = max(result, count[num] + count[num + 1])
        
        return result
