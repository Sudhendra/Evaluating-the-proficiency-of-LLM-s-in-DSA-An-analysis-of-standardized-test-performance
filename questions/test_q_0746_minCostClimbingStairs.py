import pytest
from q_0746_minCostClimbingStairs import Solution


@pytest.mark.parametrize(
    "cost, output", [([10, 15, 20], 15), ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6)]
)
class TestSolution:
    def test_minCostClimbingStairs(self, cost: List[int], output: int):
        sc = Solution()
        assert (
            sc.minCostClimbingStairs(
                cost,
            )
            == output
        )
