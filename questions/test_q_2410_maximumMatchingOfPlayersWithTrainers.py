import pytest
from q_2410_maximumMatchingOfPlayersWithTrainers import Solution


@pytest.mark.parametrize(
    "players, trainers, output", [([4, 7, 9], [8, 2, 5, 8], 2), ([1, 1, 1], [10], 1)]
)
class TestSolution:
    def test_matchPlayersAndTrainers(
        self, players: List[int], trainers: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.matchPlayersAndTrainers(
                players,
                trainers,
            )
            == output
        )
