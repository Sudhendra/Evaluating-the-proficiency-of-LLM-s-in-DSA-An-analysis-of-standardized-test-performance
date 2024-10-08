import pytest
from q_2958_lengthOfLongestSubarrayWithAtMostKFrequency import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [
        ([1, 2, 3, 1, 2, 3, 1, 2], 2, 6),
        ([1, 2, 1, 2, 1, 2, 1, 2], 1, 2),
        ([5, 5, 5, 5, 5, 5, 5], 4, 4),
    ],
)
class TestSolution:
    def test_maxSubarrayLength(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.maxSubarrayLength(
                nums,
                k,
            )
            == output
        )
