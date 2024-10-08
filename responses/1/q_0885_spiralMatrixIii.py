class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        def move_east(r, c, step):
            for _ in range(step):
                c += 1
                yield [r, c]

        def move_south(r, c, step):
            for _ in range(step):
                r += 1
                yield [r, c]

        def move_west(r, c, step):
            for _ in range(step):
                c -= 1
                yield [r, c]

        def move_north(r, c, step):
            for _ in range(step):
                r -= 1
                yield [r, c]

        res = [[rStart, cStart]]
        step = 1

        while len(res) < rows * cols:
            for _ in range(2):
                for move_func in [move_east, move_south, move_west, move_north]:
                    res.extend(list(move_func(*res[-1], step)))
                    if len(res) >= rows * cols:
                        return res
                step += 1

        return res
