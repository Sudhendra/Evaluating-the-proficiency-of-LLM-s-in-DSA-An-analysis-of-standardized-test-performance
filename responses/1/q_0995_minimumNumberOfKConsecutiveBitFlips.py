from collections import deque

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip_count = 0
        flip_queue = deque()
        
        for i in range(n):
            if flip_queue and i >= flip_queue[0] + k:
                flip_queue.popleft()
            
            if nums[i] == len(flip_queue) % 2:
                if i + k > n:
                    return -1
                flip_queue.append(i)
                flip_count += 1
        
        return flip_count