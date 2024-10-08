import pytest
from q_2448_minimumCostToMakeArrayEqual import Solution


@pytest.mark.parametrize(
    "nums, cost, output",
    [([1, 3, 5, 2], [2, 3, 1, 14], 8), ([2, 2, 2, 2, 2], [4, 2, 8, 1, 3], 0)],
)
class TestSolution:
    def test_minCost(self, nums: List[int], cost: List[int], output: int):
        sc = Solution()
        assert (
            sc.minCost(
                nums,
                cost,
            )
            == output
        )
