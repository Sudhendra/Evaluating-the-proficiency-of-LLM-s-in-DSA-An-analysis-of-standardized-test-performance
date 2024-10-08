import pytest
from q_1701_averageWaitingTime import Solution


@pytest.mark.parametrize(
    "customers, output",
    [([[1, 2], [2, 5], [4, 3]], 5.0), ([[5, 2], [5, 4], [10, 3], [20, 1]], 3.25)],
)
class TestSolution:
    def test_averageWaitingTime(self, customers: List[List[int]], output: float):
        sc = Solution()
        assert (
            sc.averageWaitingTime(
                customers,
            )
            == output
        )
