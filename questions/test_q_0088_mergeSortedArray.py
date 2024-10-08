import pytest
from q_0088_mergeSortedArray import Solution


@pytest.mark.parametrize(
    "nums1, m, nums2, n, output",
    [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
    ],
)
class TestSolution:
    def test_merge(
        self, nums1: List[int], m: int, nums2: List[int], n: int, output: None
    ):
        sc = Solution()
        assert (
            sc.merge(
                nums1,
                m,
                nums2,
                n,
            )
            == output
        )
