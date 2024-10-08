import pytest
from q_1458_maxDotProductOfTwoSubsequences import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output",
    [
        ([2, 1, -2, 5], [3, 0, -6], 18),
        ([3, -2], [2, -6, 7], 21),
        ([-1, -1], [1, 1], -1),
    ],
)
class TestSolution:
    def test_maxDotProduct(self, nums1: List[int], nums2: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxDotProduct(
                nums1,
                nums2,
            )
            == output
        )
