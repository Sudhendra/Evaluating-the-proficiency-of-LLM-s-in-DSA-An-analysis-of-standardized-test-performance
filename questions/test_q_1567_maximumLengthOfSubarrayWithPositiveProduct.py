import pytest
from q_1567_maximumLengthOfSubarrayWithPositiveProduct import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([1, -2, -3, 4], 4), ([0, 1, -2, -3, -4], 3), ([-1, -2, -3, 0, 1], 2)],
)
class TestSolution:
    def test_getMaxLen(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.getMaxLen(
                nums,
            )
            == output
        )
