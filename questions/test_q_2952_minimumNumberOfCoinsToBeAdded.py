import pytest
from q_2952_minimumNumberOfCoinsToBeAdded import Solution


@pytest.mark.parametrize(
    "coins, target, output",
    [([1, 4, 10], 19, 2), ([1, 4, 10, 5, 7, 19], 19, 1), ([1, 1, 1], 20, 3)],
)
class TestSolution:
    def test_minimumAddedCoins(self, coins: List[int], target: int, output: int):
        sc = Solution()
        assert (
            sc.minimumAddedCoins(
                coins,
                target,
            )
            == output
        )
