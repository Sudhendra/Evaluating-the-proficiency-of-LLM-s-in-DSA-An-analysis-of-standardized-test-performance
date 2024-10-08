import pytest
from q_0020_validParentheses import Solution


@pytest.mark.parametrize("s, output", [("()", True), ("()[]{}", True), ("(]", False)])
class TestSolution:
    def test_isValid(self, s: str, output: bool):
        sc = Solution()
        assert (
            sc.isValid(
                s,
            )
            == output
        )
