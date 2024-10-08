from heapq import heappush, heappop

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        max_val = max(row[0] for row in nums)
        heapq.heapify(heap)
        range_start, range_end = float('-inf'), float('inf')

        while heap:
            min_val, i, j = heappop(heap)
            if max_val - min_val < range_end - range_start:
                range_start, range_end = min_val, max_val

            if j == len(nums[i]) - 1:
                return [range_start, range_end]
            
            max_val = max(max_val, nums[i][j + 1])
            heappush(heap, (nums[i][j + 1], i, j + 1))
