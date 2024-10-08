import pytest
from q_2846_minimumEdgeWeightEquilibriumQueriesInATree import Solution


@pytest.mark.parametrize(
    "n, edges, queries, output",
    [
        (
            7,
            [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 2], [4, 5, 2], [5, 6, 2]],
            [[0, 3], [3, 6], [2, 6], [0, 6]],
            [0, 0, 1, 3],
        ),
        (
            8,
            [
                [1, 2, 6],
                [1, 3, 4],
                [2, 4, 6],
                [2, 5, 3],
                [3, 6, 6],
                [3, 0, 8],
                [7, 0, 2],
            ],
            [[4, 6], [0, 4], [6, 5], [7, 4]],
            [1, 2, 2, 3],
        ),
    ],
)
class TestSolution:
    def test_minOperationsQueries(
        self,
        n: int,
        edges: List[List[int]],
        queries: List[List[int]],
        output: List[int],
    ):
        sc = Solution()
        assert (
            sc.minOperationsQueries(
                n,
                edges,
                queries,
            )
            == output
        )
