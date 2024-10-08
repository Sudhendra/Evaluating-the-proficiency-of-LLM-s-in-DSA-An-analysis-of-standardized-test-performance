import pytest
from q_1906_minimumAbsoluteDifferenceQueries import Solution


@pytest.mark.parametrize(
    "nums, queries, output",
    [
        ([1, 3, 4, 8], [[0, 1], [1, 2], [2, 3], [0, 3]], [2, 1, 4, 1]),
        ([4, 5, 2, 2, 7, 10], [[2, 3], [0, 2], [0, 5], [3, 5]], [-1, 1, 1, 3]),
    ],
)
class TestSolution:
    def test_minDifference(
        self, nums: List[int], queries: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.minDifference(
                nums,
                queries,
            )
            == output
        )
