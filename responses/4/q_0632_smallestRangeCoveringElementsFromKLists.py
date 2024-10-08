from heapq import heappush, heappop

class Solution:
    
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        max_val = float('-inf')
        range_start, range_end = float('-inf'), float('inf')
        
        for i, row in enumerate(nums):
            heappush(heap, (row[0], i, 0))
            max_val = max(max_val, row[0])
        
        while len(heap) == len(nums):
            val, row, index = heappop(heap)
            if max_val - val < range_end - range_start:
                range_start, range_end = val, max_val
            
            if index + 1 < len(nums[row]):
                next_val = nums[row][index + 1]
                heappush(heap, (next_val, row, index + 1))
                max_val = max(max_val, next_val)
        
        return [range_start, range_end]
