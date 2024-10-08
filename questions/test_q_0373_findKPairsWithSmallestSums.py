import pytest
from q_0373_findKPairsWithSmallestSums import Solution


@pytest.mark.parametrize(
    "nums1, nums2, k, output",
    [
        ([1, 7, 11], [2, 4, 6], 3, [[1, 2], [1, 4], [1, 6]]),
        ([1, 1, 2], [1, 2, 3], 2, [[1, 1], [1, 1]]),
    ],
)
class TestSolution:
    def test_kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int, output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.kSmallestPairs(
                nums1,
                nums2,
                k,
            )
            == output
        )
