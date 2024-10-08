import pytest
from q_1568_minimumNumberOfDaysToDisconnectIsland import Solution


@pytest.mark.parametrize(
    "grid, output", [([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]], 2), ([[1, 1]], 2)]
)
class TestSolution:
    def test_minDays(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minDays(
                grid,
            )
            == output
        )
