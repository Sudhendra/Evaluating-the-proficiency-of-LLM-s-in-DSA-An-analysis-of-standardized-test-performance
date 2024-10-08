import pytest
from q_2934_minimumOperationsToMaximizeLastElementsInArrays import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output",
    [
        ([1, 2, 7], [4, 5, 3], 1),
        ([2, 3, 4, 5, 9], [8, 8, 4, 4, 4], 2),
        ([1, 5, 4], [2, 5, 3], -1),
    ],
)
class TestSolution:
    def test_minOperations(self, nums1: List[int], nums2: List[int], output: int):
        sc = Solution()
        assert (
            sc.minOperations(
                nums1,
                nums2,
            )
            == output
        )
