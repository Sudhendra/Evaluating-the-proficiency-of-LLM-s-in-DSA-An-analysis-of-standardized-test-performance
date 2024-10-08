from collections import deque

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flips = 0
        flip_count = 0
        queue = deque()

        for i in range(n):
            if queue and i >= queue[0] + k:
                queue.popleft()
                flip_count -= 1

            if (nums[i] + flip_count) % 2 == 0:
                if i + k > n:
                    return -1
                flips += 1
                flip_count += 1
                queue.append(i)

        return flips

