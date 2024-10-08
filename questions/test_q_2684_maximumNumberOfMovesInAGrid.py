import pytest
from q_2684_maximumNumberOfMovesInAGrid import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]], 3),
        ([[3, 2, 4], [2, 1, 9], [1, 1, 7]], 0),
    ],
)
class TestSolution:
    def test_maxMoves(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maxMoves(
                grid,
            )
            == output
        )
