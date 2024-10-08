import pytest
from q_0795_numberOfSubarraysWithBoundedMaximum import Solution


@pytest.mark.parametrize(
    "nums, left, right, output", [([2, 1, 4, 3], 2, 3, 3), ([2, 9, 2, 5, 6], 2, 8, 7)]
)
class TestSolution:
    def test_numSubarrayBoundedMax(
        self, nums: List[int], left: int, right: int, output: int
    ):
        sc = Solution()
        assert (
            sc.numSubarrayBoundedMax(
                nums,
                left,
                right,
            )
            == output
        )
