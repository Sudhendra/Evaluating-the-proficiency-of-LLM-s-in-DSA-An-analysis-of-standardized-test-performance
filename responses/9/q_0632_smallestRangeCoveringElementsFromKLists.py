from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(heap)
        right = max(row[0] for row in heap)
        ans = [float("-inf"), float("inf")]
        
        while True:
            left, i, j = heapq.heappop(heap)
            if right - left < ans[1] - ans[0]:
                ans = [left, right]
            if j == len(nums[i]) - 1:
                break
            heapq.heappush(heap, (nums[i][j+1], i, j+1))
            right = max(right, nums[i][j+1])
        
        return ans
