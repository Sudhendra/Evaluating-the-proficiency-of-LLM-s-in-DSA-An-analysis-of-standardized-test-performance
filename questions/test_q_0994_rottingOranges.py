import pytest
from q_0994_rottingOranges import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
        ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
        ([[0, 2]], 0),
    ],
)
class TestSolution:
    def test_orangesRotting(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.orangesRotting(
                grid,
            )
            == output
        )
