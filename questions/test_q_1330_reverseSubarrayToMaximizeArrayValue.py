import pytest
from q_1330_reverseSubarrayToMaximizeArrayValue import Solution


@pytest.mark.parametrize(
    "nums, output", [([2, 3, 1, 5, 4], 10), ([2, 4, 9, 24, 2, 1, 10], 68)]
)
class TestSolution:
    def test_maxValueAfterReverse(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxValueAfterReverse(
                nums,
            )
            == output
        )
