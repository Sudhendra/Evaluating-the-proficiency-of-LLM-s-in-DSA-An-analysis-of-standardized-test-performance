from typing import List

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        row_dict = {}
        col_dict = {}
        diag1_dict = {}
        diag2_dict = {}
        lamp_dict = {}

        for lamp in lamps:
            row, col = lamp
            row_dict[row] = row_dict.get(row, 0) + 1
            col_dict[col] = col_dict.get(col, 0) + 1
            diag1_dict[row - col] = diag1_dict.get(row - col, 0) + 1
            diag2_dict[row + col] = diag2_dict.get(row + col, 0) + 1
            lamp_dict[(row, col)] = True

        def is_illuminated(row, col):
            return row_dict.get(row, 0) > 0 or col_dict.get(col, 0) > 0 or diag1_dict.get(row - col, 0) > 0 or diag2_dict.get(row + col, 0) > 0

        def turn_off_adjacent(row, col):
            directions = [(0, 0), (0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]
            for dr, dc in directions:
                adj_row, adj_col = row + dr, col + dc
                if (adj_row, adj_col) in lamp_dict:
                    row_dict[adj_row] -= 1
                    col_dict[adj_col] -= 1
                    diag1_dict[adj_row - adj_col] -= 1
                    diag2_dict[adj_row + adj_col] -= 1
                    del lamp_dict[(adj_row, adj_col)]

        result = []
        for query_row, query_col in queries:
            query_result = 1 if is_illuminated(query_row, query_col) else 0
            result.append(query_result)
            turn_off_adjacent(query_row, query_col)

        return result
