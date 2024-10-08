class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        def is_valid(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        result = [(rStart, cStart)]
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # east, south, west, north
        steps = 1
        curr_row, curr_col = rStart, cStart
        curr_direction = 0
        
        while len(result) < rows * cols:
            if curr_direction % 2 == 0:  # for east and west directions
                for _ in range(2):
                    for _ in range(steps):
                        curr_row += direction[curr_direction][0]
                        curr_col += direction[curr_direction][1]
                        if is_valid(curr_row, curr_col):
                            result.append([curr_row, curr_col])
                    curr_direction = (curr_direction + 1) % 4
            else:  # for south and north directions
                for _ in range(2):
                    for _ in range(steps):
                        curr_row += direction[curr_direction][0]
                        curr_col += direction[curr_direction][1]
                        if is_valid(curr_row, curr_col):
                            result.append([curr_row, curr_col])
                    curr_direction = (curr_direction + 1) % 4
                steps += 1

        return result
