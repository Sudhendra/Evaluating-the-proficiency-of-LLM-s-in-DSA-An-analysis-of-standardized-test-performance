from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        window = SortedList(nums[:k])
        
        def get_median(window, k):
            if k % 2 == 0:
                return (window[k//2 - 1] + window[k//2]) / 2
            else:
                return window[k//2]
        
        result.append(get_median(window, k))
        
        for i in range(k, len(nums)):
            window.remove(nums[i - k])
            window.add(nums[i])
            result.append(get_median(window, k))
            
        return result