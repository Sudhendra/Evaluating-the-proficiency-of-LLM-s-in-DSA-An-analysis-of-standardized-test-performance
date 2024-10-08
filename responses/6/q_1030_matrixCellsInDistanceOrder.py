from typing import List

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        distance_map = []
        for r in range(rows):
            for c in range(cols):
                distance_map.append([r, c, abs(r - rCenter) + abs(c - cCenter)])
        
        distance_map.sort(key=lambda x: x[2])
        
        return [[x[0], x[1]] for x in distance_map]
