import pytest
from q_0241_differentWaysToAddParentheses import Solution


@pytest.mark.parametrize(
    "expression, output", [("2-1-1", [0, 2]), ("2*3-4*5", [-34, -14, -10, -10, 10])]
)
class TestSolution:
    def test_diffWaysToCompute(self, expression: str, output: List[int]):
        sc = Solution()
        assert (
            sc.diffWaysToCompute(
                expression,
            )
            == output
        )
