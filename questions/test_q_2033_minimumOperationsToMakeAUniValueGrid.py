import pytest
from q_2033_minimumOperationsToMakeAUniValueGrid import Solution


@pytest.mark.parametrize(
    "grid, x, output",
    [([[2, 4], [6, 8]], 2, 4), ([[1, 5], [2, 3]], 1, 5), ([[1, 2], [3, 4]], 2, -1)],
)
class TestSolution:
    def test_minOperations(self, grid: List[List[int]], x: int, output: int):
        sc = Solution()
        assert (
            sc.minOperations(
                grid,
                x,
            )
            == output
        )
