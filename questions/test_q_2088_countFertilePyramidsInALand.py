import pytest
from q_2088_countFertilePyramidsInALand import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[0, 1, 1, 0], [1, 1, 1, 1]], 2),
        ([[1, 1, 1], [1, 1, 1]], 2),
        ([[1, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 1, 0, 0, 1]], 13),
    ],
)
class TestSolution:
    def test_countPyramids(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.countPyramids(
                grid,
            )
            == output
        )
