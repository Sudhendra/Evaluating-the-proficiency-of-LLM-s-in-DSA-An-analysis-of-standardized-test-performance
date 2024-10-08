from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, total, result = defaultdict(int), 0, 0
        count[0] = 1
        
        for num in nums:
            total += num
            if total - k in count:
                result += count[total - k]
            count[total] += 1
        
        return result