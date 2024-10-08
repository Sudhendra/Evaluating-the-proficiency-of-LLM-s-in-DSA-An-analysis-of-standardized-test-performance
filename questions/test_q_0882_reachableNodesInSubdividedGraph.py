import pytest
from q_0882_reachableNodesInSubdividedGraph import Solution


@pytest.mark.parametrize(
    "edges, maxMoves, n, output",
    [
        ([[0, 1, 10], [0, 2, 1], [1, 2, 2]], 6, 3, 13),
        ([[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]], 10, 4, 23),
        ([[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4], [3, 4, 5]], 17, 5, 1),
    ],
)
class TestSolution:
    def test_reachableNodes(
        self, edges: List[List[int]], maxMoves: int, n: int, output: int
    ):
        sc = Solution()
        assert (
            sc.reachableNodes(
                edges,
                maxMoves,
                n,
            )
            == output
        )
