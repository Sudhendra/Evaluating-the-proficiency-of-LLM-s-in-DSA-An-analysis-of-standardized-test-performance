import pytest
from q_1021_removeOutermostParentheses import Solution


@pytest.mark.parametrize(
    "s, output",
    [("(()())(())", "()()()"), ("(()())(())(()(()))", "()()()()(())"), ("()()", "")],
)
class TestSolution:
    def test_removeOuterParentheses(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.removeOuterParentheses(
                s,
            )
            == output
        )
