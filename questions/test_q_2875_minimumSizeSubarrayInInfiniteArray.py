import pytest
from q_2875_minimumSizeSubarrayInInfiniteArray import Solution


@pytest.mark.parametrize(
    "nums, target, output",
    [([1, 2, 3], 5, 2), ([1, 1, 1, 2, 3], 4, 2), ([2, 4, 6, 8], 3, -1)],
)
class TestSolution:
    def test_minSizeSubarray(self, nums: List[int], target: int, output: int):
        sc = Solution()
        assert (
            sc.minSizeSubarray(
                nums,
                target,
            )
            == output
        )
