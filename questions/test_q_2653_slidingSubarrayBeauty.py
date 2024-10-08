import pytest
from q_2653_slidingSubarrayBeauty import Solution


@pytest.mark.parametrize(
    "nums, k, x, output",
    [
        ([1, -1, -3, -2, 3], 3, 2, [-1, -2, -2]),
        ([-1, -2, -3, -4, -5], 2, 2, [-1, -2, -3, -4]),
        ([-3, 1, 2, -3, 0, -3], 2, 1, [-3, 0, -3, -3, -3]),
    ],
)
class TestSolution:
    def test_getSubarrayBeauty(
        self, nums: List[int], k: int, x: int, output: List[int]
    ):
        sc = Solution()
        assert (
            sc.getSubarrayBeauty(
                nums,
                k,
                x,
            )
            == output
        )
