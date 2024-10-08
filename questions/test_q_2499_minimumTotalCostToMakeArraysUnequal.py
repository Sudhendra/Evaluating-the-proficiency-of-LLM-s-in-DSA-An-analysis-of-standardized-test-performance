import pytest
from q_2499_minimumTotalCostToMakeArraysUnequal import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output",
    [
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 10),
        ([2, 2, 2, 1, 3], [1, 2, 2, 3, 3], 10),
        ([1, 2, 2], [1, 2, 2], -1),
    ],
)
class TestSolution:
    def test_minimumTotalCost(self, nums1: List[int], nums2: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumTotalCost(
                nums1,
                nums2,
            )
            == output
        )
