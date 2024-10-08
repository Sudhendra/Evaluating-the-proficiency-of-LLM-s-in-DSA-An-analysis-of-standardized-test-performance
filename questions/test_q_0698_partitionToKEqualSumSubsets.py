import pytest
from q_0698_partitionToKEqualSumSubsets import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([4, 3, 2, 3, 5, 2, 1], 4, True), ([1, 2, 3, 4], 3, False)]
)
class TestSolution:
    def test_canPartitionKSubsets(self, nums: List[int], k: int, output: bool):
        sc = Solution()
        assert (
            sc.canPartitionKSubsets(
                nums,
                k,
            )
            == output
        )
