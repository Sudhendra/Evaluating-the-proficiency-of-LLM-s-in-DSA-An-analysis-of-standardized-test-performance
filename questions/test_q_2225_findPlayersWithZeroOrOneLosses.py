import pytest
from q_2225_findPlayersWithZeroOrOneLosses import Solution


@pytest.mark.parametrize(
    "matches, output",
    [
        (
            [
                [1, 3],
                [2, 3],
                [3, 6],
                [5, 6],
                [5, 7],
                [4, 5],
                [4, 8],
                [4, 9],
                [10, 4],
                [10, 9],
            ],
            [[1, 2, 10], [4, 5, 7, 8]],
        ),
        ([[2, 3], [1, 3], [5, 4], [6, 4]], [[1, 2, 5, 6], []]),
    ],
)
class TestSolution:
    def test_findWinners(self, matches: List[List[int]], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.findWinners(
                matches,
            )
            == output
        )
