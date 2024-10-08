import pytest
from q_2412_minimumMoneyRequiredBeforeTransactions import Solution


@pytest.mark.parametrize(
    "transactions, output", [([[2, 1], [5, 0], [4, 2]], 10), ([[3, 0], [0, 3]], 3)]
)
class TestSolution:
    def test_minimumMoney(self, transactions: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minimumMoney(
                transactions,
            )
            == output
        )
