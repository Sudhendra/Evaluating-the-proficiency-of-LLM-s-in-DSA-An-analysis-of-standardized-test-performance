from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        min_len = len(nums) + 1
        monotonous_queue = deque()

        for i in range(len(prefix_sum)):
            while monotonous_queue and prefix_sum[i] - prefix_sum[monotonous_queue[0]] >= k:
                min_len = min(min_len, i - monotonous_queue.popleft())
            while monotonous_queue and prefix_sum[i] <= prefix_sum[monotonous_queue[-1]]:
                monotonous_queue.pop()
            monotonous_queue.append(i)

        return min_len if min_len <= len(nums) else -1
