import pytest
from q_0840_magicSquaresInGrid import Solution


@pytest.mark.parametrize(
    "grid, output", [([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]], 1), ([[8]], 0)]
)
class TestSolution:
    def test_numMagicSquaresInside(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.numMagicSquaresInside(
                grid,
            )
            == output
        )
