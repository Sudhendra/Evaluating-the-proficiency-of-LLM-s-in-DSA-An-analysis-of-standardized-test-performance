import pytest
from q_1368_minimumCostToMakeAtLeastOneValidPathInAGrid import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]], 3),
        ([[1, 1, 3], [3, 2, 2], [1, 1, 4]], 0),
        ([[1, 2], [4, 3]], 1),
    ],
)
class TestSolution:
    def test_minCost(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minCost(
                grid,
            )
            == output
        )
