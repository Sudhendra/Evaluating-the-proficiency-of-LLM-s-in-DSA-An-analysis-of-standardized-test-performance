import pytest
from q_1712_waysToSplitArrayIntoThreeSubarrays import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 1, 1], 1), ([1, 2, 2, 2, 5, 0], 3), ([3, 2, 1], 0)]
)
class TestSolution:
    def test_waysToSplit(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.waysToSplit(
                nums,
            )
            == output
        )
