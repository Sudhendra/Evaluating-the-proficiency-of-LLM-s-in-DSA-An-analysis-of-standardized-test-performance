from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(arr, k):
            freq = defaultdict(int)
            left = 0
            count = 0

            for right in range(len(arr)):
                if freq[arr[right]] == 0:
                    k -= 1
                freq[arr[right]] += 1

                while k < 0:
                    freq[arr[left]] -= 1
                    if freq[arr[left]] == 0:
                        k += 1
                    left += 1

                count += right - left + 1

            return count

        return atMostK(nums, k) - atMostK(nums, k - 1)
