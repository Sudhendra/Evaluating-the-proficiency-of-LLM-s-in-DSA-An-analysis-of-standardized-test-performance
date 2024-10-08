import pytest
from q_0640_solveTheEquation import Solution


@pytest.mark.parametrize(
    "equation, output",
    [("x+5-3+x=6+x-2", "x=2"), ("x=x", "Infinite solutions"), ("2x=x", "x=0")],
)
class TestSolution:
    def test_solveEquation(self, equation: str, output: str):
        sc = Solution()
        assert (
            sc.solveEquation(
                equation,
            )
            == output
        )
