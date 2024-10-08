import pytest
from q_1905_countSubIslands import Solution


@pytest.mark.parametrize(
    "grid1, grid2, output",
    [
        (
            [
                [1, 1, 1, 0, 0],
                [0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 1, 1],
            ],
            [
                [1, 1, 1, 0, 0],
                [0, 0, 1, 1, 1],
                [0, 1, 0, 0, 0],
                [1, 0, 1, 1, 0],
                [0, 1, 0, 1, 0],
            ],
            3,
        ),
        (
            [
                [1, 0, 1, 0, 1],
                [1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [1, 0, 1, 0, 1],
            ],
            [
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0],
                [1, 0, 0, 0, 1],
            ],
            2,
        ),
    ],
)
class TestSolution:
    def test_countSubIslands(
        self, grid1: List[List[int]], grid2: List[List[int]], output: int
    ):
        sc = Solution()
        assert (
            sc.countSubIslands(
                grid1,
                grid2,
            )
            == output
        )
