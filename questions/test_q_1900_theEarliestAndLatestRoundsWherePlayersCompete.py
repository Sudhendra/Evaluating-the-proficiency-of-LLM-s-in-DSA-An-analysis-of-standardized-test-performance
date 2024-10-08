import pytest
from q_1900_theEarliestAndLatestRoundsWherePlayersCompete import Solution


@pytest.mark.parametrize(
    "n, firstPlayer, secondPlayer, output", [(11, 2, 4, [3, 4]), (5, 1, 5, [1, 1])]
)
class TestSolution:
    def test_earliestAndLatest(
        self, n: int, firstPlayer: int, secondPlayer: int, output: List[int]
    ):
        sc = Solution()
        assert (
            sc.earliestAndLatest(
                n,
                firstPlayer,
                secondPlayer,
            )
            == output
        )
