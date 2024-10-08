import pytest
from q_1896_minimumCostToChangeTheFinalValueOfExpression import Solution


@pytest.mark.parametrize(
    "expression, output", [("1&(0|1)", 1), ("(0&0)&(0&0&0)", 3), ("(0|(1|0&1))", 1)]
)
class TestSolution:
    def test_minOperationsToFlip(self, expression: str, output: int):
        sc = Solution()
        assert (
            sc.minOperationsToFlip(
                expression,
            )
            == output
        )
