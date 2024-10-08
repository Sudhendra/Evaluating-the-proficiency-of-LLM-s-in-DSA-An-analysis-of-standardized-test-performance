import pytest
from q_1169_invalidTransactions import Solution


@pytest.mark.parametrize(
    "transactions, output",
    [
        (
            ["alice,20,800,mtv", "alice,50,100,beijing"],
            ["alice,20,800,mtv", "alice,50,100,beijing"],
        ),
        (["alice,20,800,mtv", "alice,50,1200,mtv"], ["alice,50,1200,mtv"]),
        (["alice,20,800,mtv", "bob,50,1200,mtv"], ["bob,50,1200,mtv"]),
    ],
)
class TestSolution:
    def test_invalidTransactions(self, transactions: List[str], output: List[str]):
        sc = Solution()
        assert (
            sc.invalidTransactions(
                transactions,
            )
            == output
        )
