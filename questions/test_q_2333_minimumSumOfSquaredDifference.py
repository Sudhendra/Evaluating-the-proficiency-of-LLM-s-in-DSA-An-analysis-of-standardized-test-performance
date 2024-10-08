import pytest
from q_2333_minimumSumOfSquaredDifference import Solution


@pytest.mark.parametrize(
    "nums1, nums2, k1, k2, output",
    [
        ([1, 2, 3, 4], [2, 10, 20, 19], 0, 0, 579),
        ([1, 4, 10, 12], [5, 8, 6, 9], 1, 1, 43),
    ],
)
class TestSolution:
    def test_minSumSquareDiff(
        self, nums1: List[int], nums2: List[int], k1: int, k2: int, output: int
    ):
        sc = Solution()
        assert (
            sc.minSumSquareDiff(
                nums1,
                nums2,
                k1,
                k2,
            )
            == output
        )
