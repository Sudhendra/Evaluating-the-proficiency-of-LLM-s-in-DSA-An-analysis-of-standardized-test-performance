from collections import Counter

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        counter = Counter(nums)
        ans = i = 0
        
        while counter:
            if i in counter:
                del counter[i]
            else:
                ans += i - min(counter)
                i = min(counter)
        
        return ans
