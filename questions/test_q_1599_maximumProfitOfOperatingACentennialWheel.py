import pytest
from q_1599_maximumProfitOfOperatingACentennialWheel import Solution


@pytest.mark.parametrize(
    "customers, boardingCost, runningCost, output",
    [([8, 3], 5, 6, 3), ([10, 9, 6], 6, 4, 7), ([3, 4, 0, 5, 1], 1, 92, -1)],
)
class TestSolution:
    def test_minOperationsMaxProfit(
        self, customers: List[int], boardingCost: int, runningCost: int, output: int
    ):
        sc = Solution()
        assert (
            sc.minOperationsMaxProfit(
                customers,
                boardingCost,
                runningCost,
            )
            == output
        )
