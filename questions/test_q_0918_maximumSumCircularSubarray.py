import pytest
from q_0918_maximumSumCircularSubarray import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, -2, 3, -2], 3), ([5, -3, 5], 10), ([-3, -2, -3], -2)]
)
class TestSolution:
    def test_maxSubarraySumCircular(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxSubarraySumCircular(
                nums,
            )
            == output
        )
