from heapq import heapify, heappop, heappush
from collections import defaultdict

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        min_heap = []
        max_val = -10 ** 5 - 1
        range_start, range_end = -10 ** 5, 10 ** 5
        freq = defaultdict(int)
        
        for i in range(k):
            heappush(min_heap, (nums[i][0], i, 0))
            freq[nums[i][0]] += 1
            max_val = max(max_val, nums[i][0])
        
        while len(min_heap) == k:
            num, i, j = heappop(min_heap)
            if max_val - num < range_end - range_start:
                range_start, range_end = num, max_val
            
            if j + 1 < len(nums[i]):
                next_num = nums[i][j + 1]
                heappush(min_heap, (next_num, i, j + 1))
                max_val = max(max_val, next_num)
                if freq[next_num] == 0:
                    freq[next_num] = 1
                else:
                    freq[next_num] += 1
        
        return [range_start, range_end]
