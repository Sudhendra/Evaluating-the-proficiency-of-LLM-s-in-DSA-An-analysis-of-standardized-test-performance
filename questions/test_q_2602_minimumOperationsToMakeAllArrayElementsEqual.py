import pytest
from q_2602_minimumOperationsToMakeAllArrayElementsEqual import Solution


@pytest.mark.parametrize(
    "nums, queries, output",
    [([3, 1, 6, 8], [1, 5], [14, 10]), ([2, 9, 6, 3], [10], [20])],
)
class TestSolution:
    def test_minOperations(
        self, nums: List[int], queries: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.minOperations(
                nums,
                queries,
            )
            == output
        )
