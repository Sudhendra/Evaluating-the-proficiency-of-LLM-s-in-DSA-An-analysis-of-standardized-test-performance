import pytest
from q_2806_accountBalanceAfterRoundedPurchase import Solution


@pytest.mark.parametrize("purchaseAmount, output", [(9, 90), (15, 80)])
class TestSolution:
    def test_accountBalanceAfterPurchase(self, purchaseAmount: int, output: int):
        sc = Solution()
        assert (
            sc.accountBalanceAfterPurchase(
                purchaseAmount,
            )
            == output
        )
