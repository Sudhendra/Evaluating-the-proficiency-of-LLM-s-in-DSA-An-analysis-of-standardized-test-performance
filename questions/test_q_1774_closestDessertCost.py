import pytest
from q_1774_closestDessertCost import Solution


@pytest.mark.parametrize(
    "baseCosts, toppingCosts, target, output",
    [([1, 7], [3, 4], 10, 10), ([2, 3], [4, 5, 100], 18, 17), ([3, 10], [2, 5], 9, 8)],
)
class TestSolution:
    def test_closestCost(
        self, baseCosts: List[int], toppingCosts: List[int], target: int, output: int
    ):
        sc = Solution()
        assert (
            sc.closestCost(
                baseCosts,
                toppingCosts,
                target,
            )
            == output
        )
