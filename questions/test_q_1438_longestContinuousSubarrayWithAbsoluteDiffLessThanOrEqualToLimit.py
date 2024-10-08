import pytest
from q_1438_longestContinuousSubarrayWithAbsoluteDiffLessThanOrEqualToLimit import (
    Solution,
)


@pytest.mark.parametrize(
    "nums, limit, output",
    [
        ([8, 2, 4, 7], 4, 2),
        ([10, 1, 2, 4, 7, 2], 5, 4),
        ([4, 2, 2, 2, 4, 4, 2, 2], 0, 3),
    ],
)
class TestSolution:
    def test_longestSubarray(self, nums: List[int], limit: int, output: int):
        sc = Solution()
        assert (
            sc.longestSubarray(
                nums,
                limit,
            )
            == output
        )
