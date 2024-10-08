import pytest
from q_2482_differenceBetweenOnesAndZerosInRowAndColumn import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[0, 1, 1], [1, 0, 1], [0, 0, 1]], [[0, 0, 4], [0, 0, 4], [-2, -2, 2]]),
        ([[1, 1, 1], [1, 1, 1]], [[5, 5, 5], [5, 5, 5]]),
    ],
)
class TestSolution:
    def test_onesMinusZeros(self, grid: List[List[int]], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.onesMinusZeros(
                grid,
            )
            == output
        )
