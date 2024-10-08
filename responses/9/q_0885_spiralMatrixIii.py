from typing import List

class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]:
        result = []
        result.append([rStart, cStart])
        steps = 1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while len(result) < rows * cols:
            for _ in range(2):
                for i in range(steps):
                    rStart += directions[0][0]
                    cStart += directions[0][1]
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        result.append([rStart, cStart])
                directions = directions[1:] + [directions[0]]
            steps += 1
        
        return result
