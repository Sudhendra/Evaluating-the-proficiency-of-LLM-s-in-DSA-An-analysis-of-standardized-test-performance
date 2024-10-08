from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        import heapq
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(heap)
        
        left, right = float('-inf'), float('inf')
        max_val = max(row[0] for row in nums)
        
        while heap:
            val, i, j = heapq.heappop(heap)
            if max_val - val < right - left:
                left, right = val, max_val
            if j + 1 == len(nums[i]):
                return [left, right]
            next_val = nums[i][j + 1]
            max_val = max(max_val, next_val)
            heapq.heappush(heap, (next_val, i, j + 1))

# Example usage:
nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
sol = Solution()
print(sol.smallestRange(nums))
