import pytest
from q_0770_basicCalculatorIv import Solution


@pytest.mark.parametrize(
    "expression, evalvars, evalints, output",
    [
        ("e + 8 - a + 5", ["e"], [1], ["-1*a", "14"]),
        (
            "e - 8 + temperature - pressure",
            ["e", "temperature"],
            [1, 12],
            ["-1*pressure", "5"],
        ),
        ("(e + 8) * (e - 8)", [], [], ["1*e*e", "-64"]),
    ],
)
class TestSolution:
    def test_basicCalculatorIV(
        self,
        expression: str,
        evalvars: List[str],
        evalints: List[int],
        output: List[str],
    ):
        sc = Solution()
        assert (
            sc.basicCalculatorIV(
                expression,
                evalvars,
                evalints,
            )
            == output
        )
