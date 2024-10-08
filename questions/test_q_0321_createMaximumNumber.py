import pytest
from q_0321_createMaximumNumber import Solution


@pytest.mark.parametrize(
    "nums1, nums2, k, output",
    [
        ([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5, [9, 8, 6, 5, 3]),
        ([6, 7], [6, 0, 4], 5, [6, 7, 6, 0, 4]),
        ([3, 9], [8, 9], 3, [9, 8, 9]),
    ],
)
class TestSolution:
    def test_maxNumber(
        self, nums1: List[int], nums2: List[int], k: int, output: List[int]
    ):
        sc = Solution()
        assert (
            sc.maxNumber(
                nums1,
                nums2,
                k,
            )
            == output
        )
