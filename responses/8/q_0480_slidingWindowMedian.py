from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        window = SortedList(nums[:k])
        is_odd = k % 2 != 0

        for i in range(k, len(nums) + 1):
            median = window[k // 2] if is_odd else (window[k // 2 - 1] + window[k // 2]) / 2
            result.append(median)

            if i < len(nums):
                window.remove(nums[i - k])
                window.add(nums[i])

        return result
