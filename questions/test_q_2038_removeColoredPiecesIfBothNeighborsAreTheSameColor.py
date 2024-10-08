import pytest
from q_2038_removeColoredPiecesIfBothNeighborsAreTheSameColor import Solution


@pytest.mark.parametrize(
    "colors, output", [("AAABABB", True), ("AA", False), ("ABBBBBBBAAA", False)]
)
class TestSolution:
    def test_winnerOfGame(self, colors: str, output: bool):
        sc = Solution()
        assert (
            sc.winnerOfGame(
                colors,
            )
            == output
        )
