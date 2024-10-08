import pytest
from q_3036_numberOfSubarraysThatMatchAPatternIi import Solution


@pytest.mark.parametrize(
    "nums, pattern, output",
    [([1, 2, 3, 4, 5, 6], [1, 1], 4), ([1, 4, 4, 1, 3, 5, 5, 3], [1, 0, -1], 2)],
)
class TestSolution:
    def test_countMatchingSubarrays(
        self, nums: List[int], pattern: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.countMatchingSubarrays(
                nums,
                pattern,
            )
            == output
        )
