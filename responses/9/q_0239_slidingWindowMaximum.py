from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        result = []
        window = deque()

        # Adding first k elements to window
        for i in range(k):
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            window.append(i)
        
        # Processing rest of the elements
        for i in range(k, len(nums)):
            result.append(nums[window[0]])
            
            # Removing elements out of window
            if window and window[0] <= i - k:
                window.popleft()
                
            # Removing elements that are smaller than current element
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
                
            window.append(i)
        
        # Adding max of last window to result
        result.append(nums[window[0]])
        
        return result
