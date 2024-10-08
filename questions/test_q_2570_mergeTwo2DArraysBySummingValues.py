import pytest
from q_2570_mergeTwo2DArraysBySummingValues import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output",
    [
        (
            [[1, 2], [2, 3], [4, 5]],
            [[1, 4], [3, 2], [4, 1]],
            [[1, 6], [2, 3], [3, 2], [4, 6]],
        ),
        (
            [[2, 4], [3, 6], [5, 5]],
            [[1, 3], [4, 3]],
            [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]],
        ),
    ],
)
class TestSolution:
    def test_mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]], output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.mergeArrays(
                nums1,
                nums2,
            )
            == output
        )
