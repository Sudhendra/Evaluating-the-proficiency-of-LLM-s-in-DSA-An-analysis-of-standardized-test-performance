import pytest
from q_0695_maxAreaOfIsland import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        (
            [
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            ],
            6,
        ),
        ([[0, 0, 0, 0, 0, 0, 0, 0]], 0),
    ],
)
class TestSolution:
    def test_maxAreaOfIsland(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maxAreaOfIsland(
                grid,
            )
            == output
        )
