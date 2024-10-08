import pytest
from q_1688_countOfMatchesInTournament import Solution


@pytest.mark.parametrize("n, output", [(7, 6), (14, 13)])
class TestSolution:
    def test_numberOfMatches(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.numberOfMatches(
                n,
            )
            == output
        )
