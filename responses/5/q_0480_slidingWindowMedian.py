from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        window = SortedList(nums[:k])

        for i in range(k, len(nums) + 1):
            if k % 2 == 0:
                result.append((window[k // 2] + window[k // 2 - 1]) / 2)
            else:
                result.append(window[k // 2])

            if i < len(nums):
                window.add(nums[i])
                window.remove(nums[i - k])

        return result
