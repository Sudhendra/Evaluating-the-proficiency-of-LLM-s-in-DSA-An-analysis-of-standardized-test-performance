import pytest
from q_0064_minimumPathSum import Solution


@pytest.mark.parametrize(
    "grid, output",
    [([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7), ([[1, 2, 3], [4, 5, 6]], 12)],
)
class TestSolution:
    def test_minPathSum(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minPathSum(
                grid,
            )
            == output
        )
