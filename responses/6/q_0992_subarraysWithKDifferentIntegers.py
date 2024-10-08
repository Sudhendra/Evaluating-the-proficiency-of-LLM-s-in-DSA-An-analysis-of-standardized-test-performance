from collections import Counter

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostKDistinct(nums, k):
            count = Counter()
            left = 0
            result = 0

            for right in range(len(nums)):
                if count[nums[right]] == 0:
                    k -= 1
                count[nums[right]] += 1

                while k < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        k += 1
                    left += 1

                result += right - left + 1

            return result

        return atMostKDistinct(nums, k) - atMostKDistinct(nums, k - 1)
