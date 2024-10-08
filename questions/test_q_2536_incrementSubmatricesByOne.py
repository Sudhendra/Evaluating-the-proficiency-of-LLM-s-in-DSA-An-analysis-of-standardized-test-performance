import pytest
from q_2536_incrementSubmatricesByOne import Solution


@pytest.mark.parametrize(
    "n, queries, output",
    [
        (3, [[1, 1, 2, 2], [0, 0, 1, 1]], [[1, 1, 0], [1, 2, 1], [0, 1, 1]]),
        (2, [[0, 0, 1, 1]], [[1, 1], [1, 1]]),
    ],
)
class TestSolution:
    def test_rangeAddQueries(
        self, n: int, queries: List[List[int]], output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.rangeAddQueries(
                n,
                queries,
            )
            == output
        )
