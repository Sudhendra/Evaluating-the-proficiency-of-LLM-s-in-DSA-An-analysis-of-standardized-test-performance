import pytest
from q_0827_makingALargeIsland import Solution


@pytest.mark.parametrize(
    "grid, output",
    [([[1, 0], [0, 1]], 3), ([[1, 1], [1, 0]], 4), ([[1, 1], [1, 1]], 4)],
)
class TestSolution:
    def test_largestIsland(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.largestIsland(
                grid,
            )
            == output
        )
