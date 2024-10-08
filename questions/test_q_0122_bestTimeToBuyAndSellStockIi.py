import pytest
from q_0122_bestTimeToBuyAndSellStockIi import Solution


@pytest.mark.parametrize(
    "prices, output",
    [([7, 1, 5, 3, 6, 4], 7), ([1, 2, 3, 4, 5], 4), ([7, 6, 4, 3, 1], 0)],
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
