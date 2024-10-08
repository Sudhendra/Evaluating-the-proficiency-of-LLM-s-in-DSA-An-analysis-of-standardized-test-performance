import pytest
from q_1190_reverseSubstringsBetweenEachPairOfParentheses import Solution


@pytest.mark.parametrize(
    "s, output",
    [("(abcd)", "dcba"), ("(u(love)i)", "iloveu"), ("(ed(et(oc))el)", "leetcode")],
)
class TestSolution:
    def test_reverseParentheses(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.reverseParentheses(
                s,
            )
            == output
        )
