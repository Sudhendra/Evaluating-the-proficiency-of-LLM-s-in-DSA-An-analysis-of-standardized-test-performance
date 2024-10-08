class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        distance_map = []
        for i in range(rows):
            for j in range(cols):
                distance = abs(i - rCenter) + abs(j - cCenter)
                distance_map.append((distance, [i, j]))
        distance_map.sort(key=lambda x: x[0])
        return [cell[1] for cell in distance_map]