import pytest
from q_2750_waysToSplitArrayIntoGoodSubarrays import Solution


@pytest.mark.parametrize("nums, output", [([0, 1, 0, 0, 1], 3), ([0, 1, 0], 1)])
class TestSolution:
    def test_numberOfGoodSubarraySplits(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.numberOfGoodSubarraySplits(
                nums,
            )
            == output
        )
