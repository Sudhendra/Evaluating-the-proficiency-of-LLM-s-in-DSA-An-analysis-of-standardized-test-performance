import pytest
from q_0053_maximumSubarray import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6), ([1], 1), ([5, 4, -1, 7, 8], 23)],
)
class TestSolution:
    def test_maxSubArray(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxSubArray(
                nums,
            )
            == output
        )
