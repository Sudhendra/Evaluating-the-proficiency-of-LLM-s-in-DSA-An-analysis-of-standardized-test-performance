import pytest
from q_0166_fractionToRecurringDecimal import Solution


@pytest.mark.parametrize(
    "numerator, denominator, output", [(1, 2, "0.5"), (2, 1, "2"), (4, 333, "0.(012)")]
)
class TestSolution:
    def test_fractionToDecimal(self, numerator: int, denominator: int, output: str):
        sc = Solution()
        assert (
            sc.fractionToDecimal(
                numerator,
                denominator,
            )
            == output
        )
