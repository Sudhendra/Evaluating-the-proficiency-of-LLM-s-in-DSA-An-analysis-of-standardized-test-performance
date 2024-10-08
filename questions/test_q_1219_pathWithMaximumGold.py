import pytest
from q_1219_pathWithMaximumGold import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[0, 6, 0], [5, 8, 7], [0, 9, 0]], 24),
        ([[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]], 28),
    ],
)
class TestSolution:
    def test_getMaximumGold(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.getMaximumGold(
                grid,
            )
            == output
        )
