import pytest
from q_2462_totalCostToHireKWorkers import Solution


@pytest.mark.parametrize(
    "costs, k, candidates, output",
    [([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4, 11), ([1, 2, 4, 1], 3, 3, 4)],
)
class TestSolution:
    def test_totalCost(self, costs: List[int], k: int, candidates: int, output: int):
        sc = Solution()
        assert (
            sc.totalCost(
                costs,
                k,
                candidates,
            )
            == output
        )
