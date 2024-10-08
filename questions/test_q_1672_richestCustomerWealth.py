import pytest
from q_1672_richestCustomerWealth import Solution


@pytest.mark.parametrize(
    "accounts, output",
    [
        ([[1, 2, 3], [3, 2, 1]], 6),
        ([[1, 5], [7, 3], [3, 5]], 10),
        ([[2, 8, 7], [7, 1, 3], [1, 9, 5]], 17),
    ],
)
class TestSolution:
    def test_maximumWealth(self, accounts: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maximumWealth(
                accounts,
            )
            == output
        )
