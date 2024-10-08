import pytest
from q_2144_minimumCostOfBuyingCandiesWithDiscount import Solution


@pytest.mark.parametrize(
    "cost, output", [([1, 2, 3], 5), ([6, 5, 7, 9, 2, 2], 23), ([5, 5], 10)]
)
class TestSolution:
    def test_minimumCost(self, cost: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumCost(
                cost,
            )
            == output
        )
