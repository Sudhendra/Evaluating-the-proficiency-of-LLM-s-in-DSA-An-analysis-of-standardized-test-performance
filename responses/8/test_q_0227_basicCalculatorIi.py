import pytest
from q_0227_basicCalculatorIi import Solution


@pytest.mark.parametrize("s, output", [("3+2*2", 7), (" 3/2 ", 1), (" 3+5 / 2 ", 5)])
class TestSolution:
    def test_calculate(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.calculate(
                s,
            )
            == output
        )
