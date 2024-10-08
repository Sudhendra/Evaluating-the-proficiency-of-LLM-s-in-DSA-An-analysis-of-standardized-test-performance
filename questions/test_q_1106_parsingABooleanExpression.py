import pytest
from q_1106_parsingABooleanExpression import Solution


@pytest.mark.parametrize(
    "expression, output",
    [("&(|(f))", False), ("|(f,f,f,t)", True), ("!(&(f,t))", True)],
)
class TestSolution:
    def test_parseBoolExpr(self, expression: str, output: bool):
        sc = Solution()
        assert (
            sc.parseBoolExpr(
                expression,
            )
            == output
        )
