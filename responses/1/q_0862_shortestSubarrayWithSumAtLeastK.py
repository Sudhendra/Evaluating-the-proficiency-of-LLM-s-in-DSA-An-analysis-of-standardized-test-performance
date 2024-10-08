from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        min_length = float('inf')
        deque_idx = deque()
        for i in range(n + 1):
            while deque_idx and prefix_sum[i] - prefix_sum[deque_idx[0]] >= k:
                min_length = min(min_length, i - deque_idx.popleft())
            while deque_idx and prefix_sum[i] <= prefix_sum[deque_idx[-1]]:
                deque_idx.pop()
            deque_idx.append(i)
        
        return min_length if min_length != float('inf') else -1
