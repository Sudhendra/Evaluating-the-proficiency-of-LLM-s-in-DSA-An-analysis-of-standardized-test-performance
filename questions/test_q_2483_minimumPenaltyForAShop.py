import pytest
from q_2483_minimumPenaltyForAShop import Solution


@pytest.mark.parametrize("customers, output", [("YYNY", 2), ("NNNNN", 0), ("YYYY", 4)])
class TestSolution:
    def test_bestClosingTime(self, customers: str, output: int):
        sc = Solution()
        assert (
            sc.bestClosingTime(
                customers,
            )
            == output
        )
