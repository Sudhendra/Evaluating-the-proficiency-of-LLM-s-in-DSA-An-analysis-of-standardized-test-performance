from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        result = []
        window = deque()
        
        for i in range(len(nums)):
            # Remove elements outside the window
            while window and window[0] < i - k + 1:
                window.popleft()
            
            # Remove elements smaller than the current element from the end of the window
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            
            window.append(i)
            
            if i >= k - 1:
                result.append(nums[window[0]])
        
        return result
