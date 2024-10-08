import pytest
from q_0188_bestTimeToBuyAndSellStockIv import Solution


@pytest.mark.parametrize(
    "k, prices, output", [(2, [2, 4, 1], 2), (2, [3, 2, 6, 5, 0, 3], 7)]
)
class TestSolution:
    def test_maxProfit(self, k: int, prices: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxProfit(
                k,
                prices,
            )
            == output
        )
