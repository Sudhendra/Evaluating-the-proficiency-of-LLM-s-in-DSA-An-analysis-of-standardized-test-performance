from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        result = []
        window = deque()
        
        for i in range(len(nums)):
            # Remove indices that are out of the current window
            while window and window[0] < i - k + 1:
                window.popleft()
            
            # Remove indices of elements smaller than the current element
            while window and nums[i] > nums[window[-1]]:
                window.pop()
            
            window.append(i)
            
            if i >= k - 1:
                result.append(nums[window[0]])
        
        return result