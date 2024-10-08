import pytest
from q_2541_minimumOperationsToMakeArrayEqualIi import Solution


@pytest.mark.parametrize(
    "nums1, nums2, k, output",
    [([4, 3, 1, 4], [1, 3, 7, 1], 3, 2), ([3, 8, 5, 2], [2, 4, 1, 6], 1, -1)],
)
class TestSolution:
    def test_minOperations(
        self, nums1: List[int], nums2: List[int], k: int, output: int
    ):
        sc = Solution()
        assert (
            sc.minOperations(
                nums1,
                nums2,
                k,
            )
            == output
        )
