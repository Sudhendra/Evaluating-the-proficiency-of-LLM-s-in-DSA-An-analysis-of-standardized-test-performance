import pytest
from q_2389_longestSubsequenceWithLimitedSum import Solution


@pytest.mark.parametrize(
    "nums, queries, output",
    [([4, 5, 2, 1], [3, 10, 21], [2, 3, 4]), ([2, 3, 4, 5], [1], [0])],
)
class TestSolution:
    def test_answerQueries(
        self, nums: List[int], queries: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.answerQueries(
                nums,
                queries,
            )
            == output
        )
