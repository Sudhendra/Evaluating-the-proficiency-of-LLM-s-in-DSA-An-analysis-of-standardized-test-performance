import pytest
from q_0807_maxIncreaseToKeepCitySkyline import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]], 35),
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),
    ],
)
class TestSolution:
    def test_maxIncreaseKeepingSkyline(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maxIncreaseKeepingSkyline(
                grid,
            )
            == output
        )
