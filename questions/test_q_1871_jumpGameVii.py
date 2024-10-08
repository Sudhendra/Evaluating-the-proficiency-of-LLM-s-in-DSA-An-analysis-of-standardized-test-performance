import pytest
from q_1871_jumpGameVii import Solution


@pytest.mark.parametrize(
    "s, minJump, maxJump, output", [("011010", 2, 3, True), ("01101110", 2, 3, False)]
)
class TestSolution:
    def test_canReach(self, s: str, minJump: int, maxJump: int, output: bool):
        sc = Solution()
        assert (
            sc.canReach(
                s,
                minJump,
                maxJump,
            )
            == output
        )
