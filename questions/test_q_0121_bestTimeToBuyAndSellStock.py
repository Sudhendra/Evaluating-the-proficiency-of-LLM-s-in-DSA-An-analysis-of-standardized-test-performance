import pytest
from q_0121_bestTimeToBuyAndSellStock import Solution


@pytest.mark.parametrize(
    "prices, output", [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0)]
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
