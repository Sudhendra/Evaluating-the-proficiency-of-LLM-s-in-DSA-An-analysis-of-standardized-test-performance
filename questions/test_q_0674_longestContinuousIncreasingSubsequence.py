import pytest
from q_0674_longestContinuousIncreasingSubsequence import Solution


@pytest.mark.parametrize("nums, output", [([1, 3, 5, 4, 7], 3), ([2, 2, 2, 2, 2], 1)])
class TestSolution:
    def test_findLengthOfLCIS(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.findLengthOfLCIS(
                nums,
            )
            == output
        )
