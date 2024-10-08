import pytest
from q_0416_partitionEqualSubsetSum import Solution


@pytest.mark.parametrize("nums, output", [([1, 5, 11, 5], True), ([1, 2, 3, 5], False)])
class TestSolution:
    def test_canPartition(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.canPartition(
                nums,
            )
            == output
        )
