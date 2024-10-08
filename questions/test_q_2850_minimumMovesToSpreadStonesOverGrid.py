import pytest
from q_2850_minimumMovesToSpreadStonesOverGrid import Solution


@pytest.mark.parametrize(
    "grid, output",
    [([[1, 1, 0], [1, 1, 1], [1, 2, 1]], 3), ([[1, 3, 0], [1, 0, 0], [1, 0, 3]], 4)],
)
class TestSolution:
    def test_minimumMoves(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minimumMoves(
                grid,
            )
            == output
        )
