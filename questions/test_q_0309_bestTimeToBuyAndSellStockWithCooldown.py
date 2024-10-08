import pytest
from q_0309_bestTimeToBuyAndSellStockWithCooldown import Solution


@pytest.mark.parametrize("prices, output", [([1, 2, 3, 0, 2], 3), ([1], 0)])
class TestSolution:
    def test_maxProfit(self, prices: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxProfit(
                prices,
            )
            == output
        )
