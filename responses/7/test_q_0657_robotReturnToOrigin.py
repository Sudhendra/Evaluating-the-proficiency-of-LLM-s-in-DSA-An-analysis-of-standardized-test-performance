import pytest
from q_0657_robotReturnToOrigin import Solution


@pytest.mark.parametrize("moves, output", [("UD", True), ("LL", False)])
class TestSolution:
    def test_judgeCircle(self, moves: str, output: bool):
        sc = Solution()
        assert (
            sc.judgeCircle(
                moves,
            )
            == output
        )
