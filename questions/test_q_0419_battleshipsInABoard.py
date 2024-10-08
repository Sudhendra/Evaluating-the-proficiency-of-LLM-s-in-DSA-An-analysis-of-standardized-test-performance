import pytest
from q_0419_battleshipsInABoard import Solution


@pytest.mark.parametrize(
    "board, output",
    [
        ([["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]], 2),
        ([["."]], 0),
    ],
)
class TestSolution:
    def test_countBattleships(self, board: List[List[str]], output: int):
        sc = Solution()
        assert (
            sc.countBattleships(
                board,
            )
            == output
        )
