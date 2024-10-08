class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        
        if not nums:
            return []
        
        if k == 1:
            return nums
        
        q = deque()
        result = []
        
        for i in range(len(nums)):
            # Remove elements outside of the current window
            while q and q[0] < i - k + 1:
                q.popleft()
            
            # Remove elements that are smaller than the current element
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            
            q.append(i)
            
            if i >= k - 1:
                result.append(nums[q[0]])
        
        return result