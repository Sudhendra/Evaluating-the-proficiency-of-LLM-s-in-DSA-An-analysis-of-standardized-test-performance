import pytest
from q_2718_sumOfMatrixAfterQueries import Solution


@pytest.mark.parametrize(
    "n, queries, output",
    [
        (3, [[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4]], 23),
        (3, [[0, 0, 4], [0, 1, 2], [1, 0, 1], [0, 2, 3], [1, 2, 1]], 17),
    ],
)
class TestSolution:
    def test_matrixSumQueries(self, n: int, queries: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.matrixSumQueries(
                n,
                queries,
            )
            == output
        )
