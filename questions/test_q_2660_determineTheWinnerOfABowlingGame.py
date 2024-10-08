import pytest
from q_2660_determineTheWinnerOfABowlingGame import Solution


@pytest.mark.parametrize(
    "player1, player2, output",
    [
        ([4, 10, 7, 9], [6, 5, 2, 3], 1),
        ([3, 5, 7, 6], [8, 10, 10, 2], 2),
        ([2, 3], [4, 1], 0),
    ],
)
class TestSolution:
    def test_isWinner(self, player1: List[int], player2: List[int], output: int):
        sc = Solution()
        assert (
            sc.isWinner(
                player1,
                player2,
            )
            == output
        )
