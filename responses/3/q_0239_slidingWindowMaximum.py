from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        window = deque()
        
        for i in range(len(nums)):
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            window.append(i)
            
            if window[0] == i - k:
                window.popleft()
                
            if i >= k - 1:
                ans.append(nums[window[0]])
        
        return ans
