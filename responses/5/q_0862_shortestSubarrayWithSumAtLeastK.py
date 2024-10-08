from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        min_length = float('inf')
        monoq = deque()
        
        for i in range(len(prefix_sum)):
            while monoq and prefix_sum[i] - prefix_sum[monoq[0]] >= k:
                min_length = min(min_length, i - monoq.popleft())
            
            while monoq and prefix_sum[i] <= prefix_sum[monoq[-1]]:
                monoq.pop()
                
            monoq.append(i)
        
        return min_length if min_length != float('inf') else -1
