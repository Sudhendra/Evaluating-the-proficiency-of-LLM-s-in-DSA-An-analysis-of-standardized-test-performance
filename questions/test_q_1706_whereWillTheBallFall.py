import pytest
from q_1706_whereWillTheBallFall import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        (
            [
                [1, 1, 1, -1, -1],
                [1, 1, 1, -1, -1],
                [-1, -1, -1, 1, 1],
                [1, 1, 1, 1, -1],
                [-1, -1, -1, -1, -1],
            ],
            [1, -1, -1, -1, -1],
        ),
        ([[-1]], [-1]),
        (
            [
                [1, 1, 1, 1, 1, 1],
                [-1, -1, -1, -1, -1, -1],
                [1, 1, 1, 1, 1, 1],
                [-1, -1, -1, -1, -1, -1],
            ],
            [0, 1, 2, 3, 4, -1],
        ),
    ],
)
class TestSolution:
    def test_findBall(self, grid: List[List[int]], output: List[int]):
        sc = Solution()
        assert (
            sc.findBall(
                grid,
            )
            == output
        )
