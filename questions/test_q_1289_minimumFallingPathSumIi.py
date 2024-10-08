import pytest
from q_1289_minimumFallingPathSumIi import Solution


@pytest.mark.parametrize(
    "grid, output", [([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 13), ([[7]], 7)]
)
class TestSolution:
    def test_minFallingPathSum(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minFallingPathSum(
                grid,
            )
            == output
        )
