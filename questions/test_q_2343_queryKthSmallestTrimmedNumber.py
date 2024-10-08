import pytest
from q_2343_queryKthSmallestTrimmedNumber import Solution


@pytest.mark.parametrize(
    "nums, queries, output",
    [
        (["102", "473", "251", "814"], [[1, 1], [2, 3], [4, 2], [1, 2]], [2, 2, 1, 0]),
        (["24", "37", "96", "04"], [[2, 1], [2, 2]], [3, 0]),
    ],
)
class TestSolution:
    def test_smallestTrimmedNumbers(
        self, nums: List[str], queries: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.smallestTrimmedNumbers(
                nums,
                queries,
            )
            == output
        )
