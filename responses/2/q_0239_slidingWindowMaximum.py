from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_vals = []
        window = deque()
        
        for i, num in enumerate(nums):
            # Remove indices outside the window
            while window and window[0] < i - k + 1:
                window.popleft()
            
            # Remove elements in window that are smaller than current num
            while window and nums[window[-1]] < num:
                window.pop()
            
            window.append(i)
            
            if i >= k - 1:
                max_vals.append(nums[window[0]])
        
        return max_vals
