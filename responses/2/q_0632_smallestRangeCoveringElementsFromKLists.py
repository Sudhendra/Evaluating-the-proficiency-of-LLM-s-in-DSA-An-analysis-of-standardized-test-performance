from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        range_heap = [(row[0], idx, 0) for idx, row in enumerate(nums)]
        heapq.heapify(range_heap)
        
        min_range = -1e9, 1e9
        max_val = max(row[0] for row in nums)

        while True:
            min_val, list_idx, idx = heapq.heappop(range_heap)
            if max_val - min_val < min_range[1] - min_range[0]:
                min_range = [min_val, max_val]
            if idx == len(nums[list_idx]) - 1:
                break
            new_entry = (nums[list_idx][idx + 1], list_idx, idx + 1)
            heapq.heappush(range_heap, new_entry)
            max_val = max(max_val, nums[list_idx][idx + 1])

        return min_range