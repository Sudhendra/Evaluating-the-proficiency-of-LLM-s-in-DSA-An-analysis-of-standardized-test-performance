import pytest
from q_1510_stoneGameIv import Solution


@pytest.mark.parametrize("n, output", [(1, True), (2, False), (4, True)])
class TestSolution:
    def test_winnerSquareGame(self, n: int, output: bool):
        sc = Solution()
        assert (
            sc.winnerSquareGame(
                n,
            )
            == output
        )
