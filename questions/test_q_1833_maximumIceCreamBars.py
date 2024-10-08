import pytest
from q_1833_maximumIceCreamBars import Solution


@pytest.mark.parametrize(
    "costs, coins, output",
    [([1, 3, 2, 4, 1], 7, 4), ([10, 6, 8, 7, 7, 8], 5, 0), ([1, 6, 3, 1, 2, 5], 20, 6)],
)
class TestSolution:
    def test_maxIceCream(self, costs: List[int], coins: int, output: int):
        sc = Solution()
        assert (
            sc.maxIceCream(
                costs,
                coins,
            )
            == output
        )
