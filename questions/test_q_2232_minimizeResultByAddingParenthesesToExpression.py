import pytest
from q_2232_minimizeResultByAddingParenthesesToExpression import Solution


@pytest.mark.parametrize(
    "expression, output",
    [("247+38", "2(47+38)"), ("12+34", "1(2+3)4"), ("999+999", "(999+999)")],
)
class TestSolution:
    def test_minimizeResult(self, expression: str, output: str):
        sc = Solution()
        assert (
            sc.minimizeResult(
                expression,
            )
            == output
        )
