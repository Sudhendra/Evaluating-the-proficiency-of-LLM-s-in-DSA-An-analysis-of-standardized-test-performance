import pytest
from q_0678_validParenthesisString import Solution


@pytest.mark.parametrize("s, output", [("()", True), ("(*)", True), ("(*))", True)])
class TestSolution:
    def test_checkValidString(self, s: str, output: bool):
        sc = Solution()
        assert (
            sc.checkValidString(
                s,
            )
            == output
        )
