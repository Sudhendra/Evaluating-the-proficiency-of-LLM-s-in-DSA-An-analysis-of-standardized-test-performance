from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        dr, dc, step = 0, 1, 0
        
        for k in range(2*(rows + cols) - 1):
            for _ in range(k//2 + 1):
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    result.append([rStart, cStart])
                    
                if dr == 0 and dc == 1 and cStart == cols - 1 - step:
                    dr, dc = 1, 0
                elif dr == 1 and dc == 0 and rStart == rows - 1 - step:
                    dr, dc = 0, -1
                elif dr == 0 and dc == -1 and cStart == step:
                    dr, dc = -1, 0
                elif dr == -1 and dc == 0 and rStart == step + 1:
                    dr, dc = 0, 1
            
                rStart += dr
                cStart += dc
                
            if k % 2 == 1:
                step += 1
        
        return result
