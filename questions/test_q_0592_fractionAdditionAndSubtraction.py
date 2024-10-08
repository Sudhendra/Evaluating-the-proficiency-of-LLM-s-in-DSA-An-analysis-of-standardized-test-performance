import pytest
from q_0592_fractionAdditionAndSubtraction import Solution


@pytest.mark.parametrize(
    "expression, output",
    [("-1/2+1/2", "0/1"), ("-1/2+1/2+1/3", "1/3"), ("1/3-1/2", "-1/6")],
)
class TestSolution:
    def test_fractionAddition(self, expression: str, output: str):
        sc = Solution()
        assert (
            sc.fractionAddition(
                expression,
            )
            == output
        )
