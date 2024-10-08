from collections import deque

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flips = 0
        flip_indices = deque()

        for i in range(n):
            if flip_indices and i >= flip_indices[0] + k:
                flip_indices.popleft()

            if len(flip_indices) % 2 == nums[i]:
                if i + k > n:
                    return -1
                flips += 1
                flip_indices.append(i)

        return flips
