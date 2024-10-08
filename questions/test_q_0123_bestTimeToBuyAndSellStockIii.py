import pytest
from q_0123_bestTimeToBuyAndSellStockIii import Solution


@pytest.mark.parametrize(
    "prices, output",
    [([3, 3, 5, 0, 0, 3, 1, 4], 6), ([1, 2, 3, 4, 5], 4), ([7, 6, 4, 3, 1], 0)],
)
class TestSolution:
    def test_maxProfit(self, prices: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxProfit(
                prices,
            )
            == output
        )
