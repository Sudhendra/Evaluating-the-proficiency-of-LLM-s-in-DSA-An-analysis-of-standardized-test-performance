import pytest
from q_2073_timeNeededToBuyTickets import Solution


@pytest.mark.parametrize(
    "tickets, k, output", [([2, 3, 2], 2, 6), ([5, 1, 1, 1], 0, 8)]
)
class TestSolution:
    def test_timeRequiredToBuy(self, tickets: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.timeRequiredToBuy(
                tickets,
                k,
            )
            == output
        )
