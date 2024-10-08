import pytest
from q_1249_minimumRemoveToMakeValidParentheses import Solution


@pytest.mark.parametrize(
    "s, output",
    [("lee(t(c)o)de)", "lee(t(c)o)de"), ("a)b(c)d", "ab(c)d"), ("))((", "")],
)
class TestSolution:
    def test_minRemoveToMakeValid(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.minRemoveToMakeValid(
                s,
            )
            == output
        )
