import pytest
from q_2944_minimumNumberOfCoinsForFruits import Solution


@pytest.mark.parametrize("prices, output", [([3, 1, 2], 4), ([1, 10, 1, 1], 2)])
class TestSolution:
    def test_minimumCoins(self, prices: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumCoins(
                prices,
            )
            == output
        )
