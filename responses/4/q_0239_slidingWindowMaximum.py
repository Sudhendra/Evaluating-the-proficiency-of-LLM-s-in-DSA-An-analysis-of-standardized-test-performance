from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        result = []
        window = deque()
        
        for i, num in enumerate(nums):
            # Remove indexes outside the window size k
            if window and window[0] <= i - k:
                window.popleft()
            
            # Remove elements from the rear of the deque that are smaller than the current element
            while window and nums[window[-1]] < num:
                window.pop()
            
            window.append(i)
            
            # Add maximum element to the result after passing the first window
            if i >= k - 1:
                result.append(nums[window[0]])
        
        return result
