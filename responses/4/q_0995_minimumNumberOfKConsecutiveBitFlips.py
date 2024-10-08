from collections import deque

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip_count = 0
        flipped = [0] * n
        queue = deque()
        
        for i in range(n):
            if queue and i >= queue[0] + k:
                queue.popleft()
                
            if (nums[i] + sum(flipped[i:]) + len(queue)) % 2 == 0:
                if i + k > n:
                    return -1
                flip_count += 1
                queue.append(i)
                flipped[i] = 1
        
        return flip_count
