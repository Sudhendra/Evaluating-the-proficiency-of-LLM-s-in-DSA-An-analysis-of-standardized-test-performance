import pytest
from q_2110_numberOfSmoothDescentPeriodsOfAStock import Solution


@pytest.mark.parametrize(
    "prices, output", [([3, 2, 1, 4], 7), ([8, 6, 7, 7], 4), ([1], 1)]
)
class TestSolution:
    def test_getDescentPeriods(self, prices: List[int], output: int):
        sc = Solution()
        assert (
            sc.getDescentPeriods(
                prices,
            )
            == output
        )
