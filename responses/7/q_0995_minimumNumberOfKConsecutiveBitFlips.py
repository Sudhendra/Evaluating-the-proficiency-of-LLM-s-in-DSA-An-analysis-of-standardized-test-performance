from collections import deque

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        queue = deque()
        flip_count = 0

        for i in range(n):
            if queue and i >= queue[0] + k:
                queue.popleft()
            
            if len(queue) % 2 == nums[i]:
                if i + k > n:
                    return -1
                queue.append(i)
                flip_count += 1
        
        return flip_count
