import pytest
from q_2040_kthSmallestProductOfTwoSortedArrays import Solution


@pytest.mark.parametrize(
    "nums1, nums2, k, output",
    [
        ([2, 5], [3, 4], 2, 8),
        ([-4, -2, 0, 3], [2, 4], 6, 0),
        ([-2, -1, 0, 1, 2], [-3, -1, 2, 4, 5], 3, -6),
    ],
)
class TestSolution:
    def test_kthSmallestProduct(
        self, nums1: List[int], nums2: List[int], k: int, output: int
    ):
        sc = Solution()
        assert (
            sc.kthSmallestProduct(
                nums1,
                nums2,
                k,
            )
            == output
        )
