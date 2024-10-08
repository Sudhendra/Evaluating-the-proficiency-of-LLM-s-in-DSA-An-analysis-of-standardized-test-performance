import pytest
from q_0518_coinChangeIi import Solution


@pytest.mark.parametrize(
    "amount, coins, output", [(5, [1, 2, 5], 4), (3, [2], 0), (10, [10], 1)]
)
class TestSolution:
    def test_change(self, amount: int, coins: List[int], output: int):
        sc = Solution()
        assert (
            sc.change(
                amount,
                coins,
            )
            == output
        )
