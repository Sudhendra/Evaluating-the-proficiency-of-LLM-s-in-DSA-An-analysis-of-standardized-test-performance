from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        pointers = [0] * k
        min_range = float('-inf')
        max_val = max(nums[i][0] for i in range(k))

        while True:
            min_val = min(nums[i][pointers[i]] for i in range(k))
            max_val = max(nums[i][pointers[i]] for i in range(k))

            if max_val - min_val < max_val - min_range:
                min_range = min_val

            min_idx = min(range(k), key=lambda i: nums[i][pointers[i]])
            pointers[min_idx] += 1
            if pointers[min_idx] == len(nums[min_idx]):
                break

        return [min_range, max_val]