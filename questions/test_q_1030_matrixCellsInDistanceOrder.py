import pytest
from q_1030_matrixCellsInDistanceOrder import Solution


@pytest.mark.parametrize(
    "rows, cols, rCenter, cCenter, output",
    [
        (1, 2, 0, 0, [[0, 0], [0, 1]]),
        (2, 2, 0, 1, [[0, 1], [0, 0], [1, 1], [1, 0]]),
        (2, 3, 1, 2, [[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]),
    ],
)
class TestSolution:
    def test_allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int, output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.allCellsDistOrder(
                rows,
                cols,
                rCenter,
                cCenter,
            )
            == output
        )
