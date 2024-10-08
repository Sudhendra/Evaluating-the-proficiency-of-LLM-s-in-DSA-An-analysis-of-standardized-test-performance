from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        min_length = float('inf')
        mono_queue = deque()
        
        for i in range(n+1):
            while mono_queue and prefix_sum[i] - prefix_sum[mono_queue[0]] >= k:
                min_length = min(min_length, i - mono_queue.popleft())
            
            while mono_queue and prefix_sum[i] <= prefix_sum[mono_queue[-1]]:
                mono_queue.pop()
                
            mono_queue.append(i)
        
        return min_length if min_length != float('inf') else -1
