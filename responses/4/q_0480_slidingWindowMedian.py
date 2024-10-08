from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        window = SortedList(nums[:k])

        def get_median(window):
            n = len(window)
            if n % 2 == 0:
                return (window[n // 2 - 1] + window[n // 2]) / 2
            else:
                return window[n // 2]

        result.append(get_median(window))

        for i in range(k, len(nums)):
            window.discard(nums[i - k])
            window.add(nums[i])
            result.append(get_median(window))

        return result
