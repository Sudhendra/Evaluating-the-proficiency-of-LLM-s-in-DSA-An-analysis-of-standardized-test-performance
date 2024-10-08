import pytest
from q_2017_gridGame import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[2, 5, 4], [1, 5, 1]], 4),
        ([[3, 3, 1], [8, 5, 2]], 4),
        ([[1, 3, 1, 15], [1, 3, 3, 1]], 7),
    ],
)
class TestSolution:
    def test_gridGame(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.gridGame(
                grid,
            )
            == output
        )
