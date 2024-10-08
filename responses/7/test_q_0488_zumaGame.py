import pytest
from q_0488_zumaGame import Solution


@pytest.mark.parametrize(
    "board, hand, output",
    [("WRRBBW", "RB", -1), ("WWRRBBWW", "WRBRW", 2), ("G", "GGGGG", 2)],
)
class TestSolution:
    def test_findMinStep(self, board: str, hand: str, output: int):
        sc = Solution()
        assert (
            sc.findMinStep(
                board,
                hand,
            )
            == output
        )
