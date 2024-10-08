import pytest
from q_2542_maximumSubsequenceScore import Solution


@pytest.mark.parametrize(
    "nums1, nums2, k, output",
    [([1, 3, 3, 2], [2, 1, 3, 4], 3, 12), ([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1, 30)],
)
class TestSolution:
    def test_maxScore(self, nums1: List[int], nums2: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.maxScore(
                nums1,
                nums2,
                k,
            )
            == output
        )
