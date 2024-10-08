from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        min_len = float('inf')
        monoq = deque()
        for i in range(n+1):
            while monoq and prefix_sum[i] - prefix_sum[monoq[0]] >= k:
                min_len = min(min_len, i - monoq.popleft())
            while monoq and prefix_sum[i] <= prefix_sum[monoq[-1]]:
                monoq.pop()
            monoq.append(i)

        return min_len if min_len != float('inf') else -1
