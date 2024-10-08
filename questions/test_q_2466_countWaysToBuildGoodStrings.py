import pytest
from q_2466_countWaysToBuildGoodStrings import Solution


@pytest.mark.parametrize(
    "low, high, zero, one, output", [(3, 3, 1, 1, 8), (2, 3, 1, 2, 5)]
)
class TestSolution:
    def test_countGoodStrings(
        self, low: int, high: int, zero: int, one: int, output: int
    ):
        sc = Solution()
        assert (
            sc.countGoodStrings(
                low,
                high,
                zero,
                one,
            )
            == output
        )
