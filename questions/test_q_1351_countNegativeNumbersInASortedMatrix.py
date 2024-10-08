import pytest
from q_1351_countNegativeNumbersInASortedMatrix import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]], 8),
        ([[3, 2], [1, 0]], 0),
    ],
)
class TestSolution:
    def test_countNegatives(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.countNegatives(
                grid,
            )
            == output
        )
