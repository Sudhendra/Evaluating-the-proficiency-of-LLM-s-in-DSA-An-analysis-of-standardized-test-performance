from typing import List
import pytest
from q_0885_spiralMatrixIii import Solution


@pytest.mark.parametrize(
    "rows, cols, rStart, cStart, output",
    [
        (1, 4, 0, 0, [[0, 0], [0, 1], [0, 2], [0, 3]]),
        (
            5,
            6,
            1,
            4,
            [
                [1, 4],
                [1, 5],
                [2, 5],
                [2, 4],
                [2, 3],
                [1, 3],
                [0, 3],
                [0, 4],
                [0, 5],
                [3, 5],
                [3, 4],
                [3, 3],
                [3, 2],
                [2, 2],
                [1, 2],
                [0, 2],
                [4, 5],
                [4, 4],
                [4, 3],
                [4, 2],
                [4, 1],
                [3, 1],
                [2, 1],
                [1, 1],
                [0, 1],
                [4, 0],
                [3, 0],
                [2, 0],
                [1, 0],
                [0, 0],
            ],
        ),
    ],
)
class TestSolution:
    def test_spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int, output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.spiralMatrixIII(
                rows,
                cols,
                rStart,
                cStart,
            )
            == output
        )
