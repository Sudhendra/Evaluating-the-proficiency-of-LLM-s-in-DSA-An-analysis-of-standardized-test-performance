from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        min_len = float('inf')
        monoq = deque()
        
        for j in range(n + 1):
            while monoq and prefix_sum[j] - prefix_sum[monoq[0]] >= k:
                min_len = min(min_len, j - monoq.popleft())
            while monoq and prefix_sum[j] <= prefix_sum[monoq[-1]]:
                monoq.pop()
            monoq.append(j)
        
        return min_len if min_len != float('inf') else -1
