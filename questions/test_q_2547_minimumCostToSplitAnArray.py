import pytest
from q_2547_minimumCostToSplitAnArray import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [([1, 2, 1, 2, 1, 3, 3], 2, 8), ([1, 2, 1, 2, 1], 2, 6), ([1, 2, 1, 2, 1], 5, 10)],
)
class TestSolution:
    def test_minCost(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.minCost(
                nums,
                k,
            )
            == output
        )
