import pytest
from q_0673_numberOfLongestIncreasingSubsequence import Solution


@pytest.mark.parametrize("nums, output", [([1, 3, 5, 4, 7], 2), ([2, 2, 2, 2, 2], 5)])
class TestSolution:
    def test_findNumberOfLIS(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.findNumberOfLIS(
                nums,
            )
            == output
        )
