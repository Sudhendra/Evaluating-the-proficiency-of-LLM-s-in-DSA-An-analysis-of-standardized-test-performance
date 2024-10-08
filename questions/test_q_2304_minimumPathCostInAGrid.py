import pytest
from q_2304_minimumPathCostInAGrid import Solution


@pytest.mark.parametrize(
    "grid, moveCost, output",
    [
        (
            [[5, 3], [4, 0], [2, 1]],
            [[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]],
            17,
        ),
        (
            [[5, 1, 2], [4, 0, 3]],
            [[12, 10, 15], [20, 23, 8], [21, 7, 1], [8, 1, 13], [9, 10, 25], [5, 3, 2]],
            6,
        ),
    ],
)
class TestSolution:
    def test_minPathCost(
        self, grid: List[List[int]], moveCost: List[List[int]], output: int
    ):
        sc = Solution()
        assert (
            sc.minPathCost(
                grid,
                moveCost,
            )
            == output
        )
