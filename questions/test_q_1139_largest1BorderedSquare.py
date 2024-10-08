import pytest
from q_1139_largest1BorderedSquare import Solution


@pytest.mark.parametrize(
    "grid, output", [([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 9), ([[1, 1, 0, 0]], 1)]
)
class TestSolution:
    def test_largest1BorderedSquare(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.largest1BorderedSquare(
                grid,
            )
            == output
        )
