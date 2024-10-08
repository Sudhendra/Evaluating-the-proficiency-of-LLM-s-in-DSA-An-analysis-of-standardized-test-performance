import pytest
from q_3010_divideAnArrayIntoSubarraysWithMinimumCostI import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 3, 12], 6), ([5, 4, 3], 12), ([10, 3, 1, 1], 12)]
)
class TestSolution:
    def test_minimumCost(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumCost(
                nums,
            )
            == output
        )
