import pytest
from q_2316_countUnreachablePairsOfNodesInAnUndirectedGraph import Solution


@pytest.mark.parametrize(
    "n, edges, output",
    [
        (3, [[0, 1], [0, 2], [1, 2]], 0),
        (7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]], 14),
    ],
)
class TestSolution:
    def test_countPairs(self, n: int, edges: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.countPairs(
                n,
                edges,
            )
            == output
        )
