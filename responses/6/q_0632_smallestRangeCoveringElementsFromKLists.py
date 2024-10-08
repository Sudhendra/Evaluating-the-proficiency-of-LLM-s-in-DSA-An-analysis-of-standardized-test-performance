from heapq import heappush, heappop

class Solution:
    
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        max_val = float('-inf')
        range_start = range_end = -1
        
        # Initialize heap with first element from each sorted list
        for i, lst in enumerate(nums):
            heappush(heap, (lst[0], i, 0))
            max_val = max(max_val, lst[0])
        
        while heap:
            val, list_idx, idx = heappop(heap)
            if max_val - val < range_end - range_start or range_start == -1:
                range_start, range_end = val, max_val
            
            if idx + 1 < len(nums[list_idx]):
                next_val = nums[list_idx][idx + 1]
                heappush(heap, (next_val, list_idx, idx + 1))
                max_val = max(max_val, next_val)
            else:
                break
        
        return [range_start, range_end]
