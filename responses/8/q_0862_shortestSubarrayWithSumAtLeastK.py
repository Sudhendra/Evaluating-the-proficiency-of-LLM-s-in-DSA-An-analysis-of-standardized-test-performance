from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        min_len = float('inf')
        queue = deque()
        
        for i in range(n+1):
            while queue and prefix_sum[i] - prefix_sum[queue[0]] >= k:
                min_len = min(min_len, i - queue.popleft())
                
            while queue and prefix_sum[i] <= prefix_sum[queue[-1]]:
                queue.pop()
                
            queue.append(i)
        
        return min_len if min_len != float('inf') else -1
