import pytest
from q_2915_lengthOfTheLongestSubsequenceThatSumsToTarget import Solution


@pytest.mark.parametrize(
    "nums, target, output",
    [([1, 2, 3, 4, 5], 9, 3), ([4, 1, 3, 2, 1, 5], 7, 4), ([1, 1, 5, 4, 5], 3, -1)],
)
class TestSolution:
    def test_lengthOfLongestSubsequence(
        self, nums: List[int], target: int, output: int
    ):
        sc = Solution()
        assert (
            sc.lengthOfLongestSubsequence(
                nums,
                target,
            )
            == output
        )
