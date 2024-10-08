import pytest
from q_1895_largestMagicSquare import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]], 3),
        ([[5, 1, 3, 1], [9, 3, 3, 1], [1, 3, 3, 8]], 2),
    ],
)
class TestSolution:
    def test_largestMagicSquare(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.largestMagicSquare(
                grid,
            )
            == output
        )
