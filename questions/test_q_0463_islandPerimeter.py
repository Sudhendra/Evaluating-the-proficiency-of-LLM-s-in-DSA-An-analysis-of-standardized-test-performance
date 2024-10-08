import pytest
from q_0463_islandPerimeter import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]], 16),
        ([[1]], 4),
        ([[1, 0]], 4),
    ],
)
class TestSolution:
    def test_islandPerimeter(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.islandPerimeter(
                grid,
            )
            == output
        )
