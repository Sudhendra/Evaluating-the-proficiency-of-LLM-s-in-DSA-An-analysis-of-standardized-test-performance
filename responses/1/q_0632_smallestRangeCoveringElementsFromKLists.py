from heapq import heappush, heappop

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        max_val = float('-inf')
        for i, row in enumerate(nums):
            heappush(min_heap, (row[0], i, 0))
            max_val = max(max_val, row[0])
        
        start, end = float('-inf'), float('inf')
        
        while len(min_heap) == len(nums):
            val, row, index = heappop(min_heap)
            if max_val - val < end - start:
                start, end = val, max_val
                
            if index + 1 < len(nums[row]):
                next_val = nums[row][index + 1]
                heappush(min_heap, (next_val, row, index + 1))
                max_val = max(max_val, next_val)
        
        return [start, end]
