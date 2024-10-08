import pytest
from q_1561_maximumNumberOfCoinsYouCanGet import Solution


@pytest.mark.parametrize(
    "piles, output",
    [([2, 4, 1, 2, 7, 8], 9), ([2, 4, 5], 4), ([9, 8, 7, 6, 5, 1, 2, 3, 4], 18)],
)
class TestSolution:
    def test_maxCoins(self, piles: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxCoins(
                piles,
            )
            == output
        )
