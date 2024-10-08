import pytest
from q_2328_numberOfIncreasingPathsInAGrid import Solution


@pytest.mark.parametrize("grid, output", [([[1, 1], [3, 4]], 8), ([[1], [2]], 3)])
class TestSolution:
    def test_countPaths(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.countPaths(
                grid,
            )
            == output
        )
