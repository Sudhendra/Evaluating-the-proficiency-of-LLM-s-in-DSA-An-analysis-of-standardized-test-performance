import pytest
from q_0150_evaluateReversePolishNotation import Solution


@pytest.mark.parametrize(
    "tokens, output",
    [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ],
)
class TestSolution:
    def test_evalRPN(self, tokens: List[str], output: int):
        sc = Solution()
        assert (
            sc.evalRPN(
                tokens,
            )
            == output
        )
