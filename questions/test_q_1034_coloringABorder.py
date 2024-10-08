import pytest
from q_1034_coloringABorder import Solution


@pytest.mark.parametrize(
    "grid, row, col, color, output",
    [
        ([[1, 1], [1, 2]], 0, 0, 3, [[3, 3], [3, 2]]),
        ([[1, 2, 2], [2, 3, 2]], 0, 1, 3, [[1, 3, 3], [2, 3, 3]]),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 1, 2, [[2, 2, 2], [2, 1, 2], [2, 2, 2]]),
    ],
)
class TestSolution:
    def test_colorBorder(
        self,
        grid: List[List[int]],
        row: int,
        col: int,
        color: int,
        output: List[List[int]],
    ):
        sc = Solution()
        assert (
            sc.colorBorder(
                grid,
                row,
                col,
                color,
            )
            == output
        )
