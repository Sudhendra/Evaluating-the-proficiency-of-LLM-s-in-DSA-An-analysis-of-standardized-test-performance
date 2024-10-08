import pytest
from q_2956_findCommonElementsBetweenTwoArrays import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output",
    [([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6], [3, 4]), ([3, 4, 2, 3], [1, 5], [0, 0])],
)
class TestSolution:
    def test_findIntersectionValues(
        self, nums1: List[int], nums2: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.findIntersectionValues(
                nums1,
                nums2,
            )
            == output
        )
