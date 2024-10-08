import pytest
from q_2706_buyTwoChocolates import Solution


@pytest.mark.parametrize(
    "prices, money, output", [([1, 2, 2], 3, 0), ([3, 2, 3], 3, 3)]
)
class TestSolution:
    def test_buyChoco(self, prices: List[int], money: int, output: int):
        sc = Solution()
        assert (
            sc.buyChoco(
                prices,
                money,
            )
            == output
        )
