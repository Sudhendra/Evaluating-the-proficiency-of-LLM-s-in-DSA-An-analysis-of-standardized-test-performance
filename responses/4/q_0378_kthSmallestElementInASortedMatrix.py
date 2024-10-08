from heapq import heappush, heappop

class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        heap = [(matrix[i][0], i, 0) for i in range(n)]
        heapify(heap)
        
        for _ in range(k-1):
            val, i, j = heappop(heap)
            if j+1 < n:
                heappush(heap, (matrix[i][j+1], i, j+1))
        
        return heappop(heap)[0]
