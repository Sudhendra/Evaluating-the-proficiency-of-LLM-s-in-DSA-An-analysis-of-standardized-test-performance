from collections import deque

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flipped = 0
        queue = deque()

        for i in range(n):
            if queue and i >= queue[0] + k:
                queue.popleft()

            if len(queue) % 2 == nums[i]:
                if i + k > n:
                    return -1
                queue.append(i)
                flipped += 1
        
        return flipped
