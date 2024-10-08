import pytest
from q_0322_coinChange import Solution


@pytest.mark.parametrize(
    "coins, amount, output", [([1, 2, 5], 11, 3), ([2], 3, -1), ([1], 0, 0)]
)
class TestSolution:
    def test_coinChange(self, coins: List[int], amount: int, output: int):
        sc = Solution()
        assert (
            sc.coinChange(
                coins,
                amount,
            )
            == output
        )
