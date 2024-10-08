import pytest
from q_0417_pacificAtlanticWaterFlow import Solution


@pytest.mark.parametrize(
    "heights, output",
    [
        (
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ],
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
        ),
        ([[1]], [[0, 0]]),
    ],
)
class TestSolution:
    def test_pacificAtlantic(self, heights: List[List[int]], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.pacificAtlantic(
                heights,
            )
            == output
        )
