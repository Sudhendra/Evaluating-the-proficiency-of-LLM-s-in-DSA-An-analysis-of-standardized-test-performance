import pytest
from q_2918_minimumEqualSumOfTwoArraysAfterReplacingZeros import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output",
    [([3, 2, 0, 1, 0], [6, 5, 0], 12), ([2, 0, 2, 0], [1, 4], -1)],
)
class TestSolution:
    def test_minSum(self, nums1: List[int], nums2: List[int], output: int):
        sc = Solution()
        assert (
            sc.minSum(
                nums1,
                nums2,
            )
            == output
        )
