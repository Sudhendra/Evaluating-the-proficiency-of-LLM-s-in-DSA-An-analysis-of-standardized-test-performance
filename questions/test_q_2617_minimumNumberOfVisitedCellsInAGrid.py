import pytest
from q_2617_minimumNumberOfVisitedCellsInAGrid import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[3, 4, 2, 1], [4, 2, 3, 1], [2, 1, 0, 0], [2, 4, 0, 0]], 4),
        ([[3, 4, 2, 1], [4, 2, 1, 1], [2, 1, 1, 0], [3, 4, 1, 0]], 3),
        ([[2, 1, 0], [1, 0, 0]], -1),
    ],
)
class TestSolution:
    def test_minimumVisitedCells(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minimumVisitedCells(
                grid,
            )
            == output
        )
