import pytest
from q_0985_sumOfEvenNumbersAfterQueries import Solution


@pytest.mark.parametrize(
    "nums, queries, output",
    [
        ([1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]], [8, 6, 2, 4]),
        ([1], [[4, 0]], [0]),
    ],
)
class TestSolution:
    def test_sumEvenAfterQueries(
        self, nums: List[int], queries: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.sumEvenAfterQueries(
                nums,
                queries,
            )
            == output
        )
