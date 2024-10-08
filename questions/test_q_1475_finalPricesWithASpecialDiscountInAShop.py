import pytest
from q_1475_finalPricesWithASpecialDiscountInAShop import Solution


@pytest.mark.parametrize(
    "prices, output",
    [
        ([8, 4, 6, 2, 3], [4, 2, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([10, 1, 1, 6], [9, 0, 1, 6]),
    ],
)
class TestSolution:
    def test_finalPrices(self, prices: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.finalPrices(
                prices,
            )
            == output
        )
