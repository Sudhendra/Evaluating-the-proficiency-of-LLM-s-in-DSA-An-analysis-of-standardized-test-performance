import pytest
from q_2771_longestNonDecreasingSubarrayFromTwoArrays import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output",
    [([2, 3, 1], [1, 2, 1], 2), ([1, 3, 2, 1], [2, 2, 3, 4], 4), ([1, 1], [2, 2], 2)],
)
class TestSolution:
    def test_maxNonDecreasingLength(
        self, nums1: List[int], nums2: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.maxNonDecreasingLength(
                nums1,
                nums2,
            )
            == output
        )
