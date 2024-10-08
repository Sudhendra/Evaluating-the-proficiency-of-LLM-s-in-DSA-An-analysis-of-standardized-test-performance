import pytest
from q_0714_bestTimeToBuyAndSellStockWithTransactionFee import Solution


@pytest.mark.parametrize(
    "prices, fee, output", [([1, 3, 2, 8, 4, 9], 2, 8), ([1, 3, 7, 5, 10, 3], 3, 6)]
)
class TestSolution:
    def test_maxProfit(self, prices: List[int], fee: int, output: int):
        sc = Solution()
        assert (
            sc.maxProfit(
                prices,
                fee,
            )
            == output
        )
