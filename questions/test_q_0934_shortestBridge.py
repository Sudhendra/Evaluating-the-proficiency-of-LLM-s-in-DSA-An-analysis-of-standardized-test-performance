import pytest
from q_0934_shortestBridge import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[0, 1], [1, 0]], 1),
        ([[0, 1, 0], [0, 0, 0], [0, 0, 1]], 2),
        (
            [
                [1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1],
            ],
            1,
        ),
    ],
)
class TestSolution:
    def test_shortestBridge(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.shortestBridge(
                grid,
            )
            == output
        )
