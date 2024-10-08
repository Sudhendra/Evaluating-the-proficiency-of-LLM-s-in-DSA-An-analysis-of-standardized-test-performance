import pytest
from q_0300_longestIncreasingSubsequence import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
    ],
)
class TestSolution:
    def test_lengthOfLIS(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.lengthOfLIS(
                nums,
            )
            == output
        )
