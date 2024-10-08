import pytest
from q_0004_medianOfTwoSortedArrays import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output", [([1, 3], [2], 2.0), ([1, 2], [3, 4], 2.5)]
)
class TestSolution:
    def test_findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int], output: float
    ):
        sc = Solution()
        assert (
            sc.findMedianSortedArrays(
                nums1,
                nums2,
            )
            == output
        )
