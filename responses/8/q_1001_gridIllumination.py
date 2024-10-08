from typing import List

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        def illuminate(row, col):
            nonlocal lamps_set
            lamps_set.add((row, col))
            row_lamps[row] += 1
            col_lamps[col] += 1
            diag_lamps[row - col] += 1
            anti_diag_lamps[row + col] += 1
        
        def turn_off(row, col):
            nonlocal lamps_set
            lamps_set.remove((row, col))
            row_lamps[row] -= 1
            col_lamps[col] -= 1
            diag_lamps[row - col] -= 1
            anti_diag_lamps[row + col] -= 1
            
        def is_illuminated(row, col):
            return row_lamps[row] > 0 or col_lamps[col] > 0 or diag_lamps[row - col] > 0 or anti_diag_lamps[row + col] > 0
        
        lamps_set = set()
        row_lamps = [0] * n
        col_lamps = [0] * n
        diag_lamps = [0] * (2 * n - 1)
        anti_diag_lamps = [0] * (2 * n - 1)
        
        for lamp in lamps:
            illuminate(lamp[0], lamp[1])
        
        result = []
        for query in queries:
            row, col = query[0], query[1]
            
            result.append(1 if is_illuminated(row, col) else 0)
            
            for i in range(row-1, row+2):
                for j in range(col-1, col+2):
                    if (i, j) in lamps_set:
                        turn_off(i, j)
        
        return result
