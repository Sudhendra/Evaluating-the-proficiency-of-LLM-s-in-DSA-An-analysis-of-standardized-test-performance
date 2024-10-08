from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        deque_idx = deque()
        ans = float('inf')
        for i in range(n+1):
            while deque_idx and prefix_sum[i] - prefix_sum[deque_idx[0]] >= k:
                ans = min(ans, i - deque_idx.popleft())
            while deque_idx and prefix_sum[i] <= prefix_sum[deque_idx[-1]]:
                deque_idx.pop()
            deque_idx.append(i)
        return ans if ans != float('inf') else -1
