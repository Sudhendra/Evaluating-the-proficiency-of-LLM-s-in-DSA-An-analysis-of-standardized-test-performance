import pytest
from q_2352_equalRowAndColumnPairs import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[3, 2, 1], [1, 7, 6], [2, 7, 7]], 1),
        ([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]], 3),
    ],
)
class TestSolution:
    def test_equalPairs(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.equalPairs(
                grid,
            )
            == output
        )
