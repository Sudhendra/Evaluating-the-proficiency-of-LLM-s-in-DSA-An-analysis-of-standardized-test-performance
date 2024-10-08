import pytest
from q_0301_removeInvalidParentheses import Solution


@pytest.mark.parametrize(
    "s, output",
    [
        ("()())()", ["(())()", "()()()"]),
        ("(a)())()", ["(a())()", "(a)()()"]),
        (")(", [""]),
    ],
)
class TestSolution:
    def test_removeInvalidParentheses(self, s: str, output: List[str]):
        sc = Solution()
        assert (
            sc.removeInvalidParentheses(
                s,
            )
            == output
        )
