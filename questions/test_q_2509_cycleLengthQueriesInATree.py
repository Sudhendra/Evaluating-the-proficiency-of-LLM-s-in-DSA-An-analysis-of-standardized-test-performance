import pytest
from q_2509_cycleLengthQueriesInATree import Solution


@pytest.mark.parametrize(
    "n, queries, output", [(3, [[5, 3], [4, 7], [2, 3]], [4, 5, 3]), (2, [[1, 2]], [2])]
)
class TestSolution:
    def test_cycleLengthQueries(
        self, n: int, queries: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.cycleLengthQueries(
                n,
                queries,
            )
            == output
        )
