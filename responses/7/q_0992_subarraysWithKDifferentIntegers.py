from collections import Counter

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostKDistinct(nums, k) - self.atMostKDistinct(nums, k - 1)
    
    def atMostKDistinct(self, nums: List[int], k: int) -> int:
        counter = Counter()
        left = 0
        result = 0

        for right in range(len(nums)):
            if counter[nums[right]] == 0:
                k -= 1
            counter[nums[right]] += 1

            while k < 0:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    k += 1
                left += 1
            
            result += right - left + 1

        return result
