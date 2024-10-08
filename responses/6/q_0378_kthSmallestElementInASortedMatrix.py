from heapq import heappush, heappop

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        
        for i in range(min(k, n)):
            heappush(heap, (matrix[i][0], i, 0))
        
        while k:
            element, row, col = heappop(heap)
            if col < n - 1:
                heappush(heap, (matrix[row][col + 1], row, col + 1))
            k -= 1
        
        return element
