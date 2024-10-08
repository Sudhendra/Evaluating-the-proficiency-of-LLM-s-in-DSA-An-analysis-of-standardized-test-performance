import pytest
from q_0796_rotateString import Solution


@pytest.mark.parametrize(
    "s, goal, output", [("abcde", "cdeab", True), ("abcde", "abced", False)]
)
class TestSolution:
    def test_rotateString(self, s: str, goal: str, output: bool):
        sc = Solution()
        assert (
            sc.rotateString(
                s,
                goal,
            )
            == output
        )
