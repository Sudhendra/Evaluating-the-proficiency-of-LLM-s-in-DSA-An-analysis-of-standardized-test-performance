import pytest
from q_2736_maximumSumQueries import Solution


@pytest.mark.parametrize(
    "nums1, nums2, queries, output",
    [
        ([4, 3, 1, 2], [2, 4, 9, 5], [[4, 1], [1, 3], [2, 5]], [6, 10, 7]),
        ([3, 2, 5], [2, 3, 4], [[4, 4], [3, 2], [1, 1]], [9, 9, 9]),
        ([2, 1], [2, 3], [[3, 3]], [-1]),
    ],
)
class TestSolution:
    def test_maximumSumQueries(
        self,
        nums1: List[int],
        nums2: List[int],
        queries: List[List[int]],
        output: List[int],
    ):
        sc = Solution()
        assert (
            sc.maximumSumQueries(
                nums1,
                nums2,
                queries,
            )
            == output
        )
