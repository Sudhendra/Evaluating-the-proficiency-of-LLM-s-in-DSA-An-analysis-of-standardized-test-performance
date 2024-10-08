from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            count = defaultdict(int)
            left = result = subarrays = 0

            for right in range(len(nums)):
                if count[nums[right]] == 0:
                    k -= 1
                count[nums[right]] += 1

                while k < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        k += 1
                    left += 1

                subarrays += right - left + 1
                result += subarrays

            return result

        return atMostK(nums, k) - atMostK(nums, k - 1)
