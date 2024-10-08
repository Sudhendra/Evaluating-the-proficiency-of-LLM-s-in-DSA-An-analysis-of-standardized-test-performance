import pytest
from q_2858_minimumEdgeReversalsSoEveryNodeIsReachable import Solution


@pytest.mark.parametrize(
    "n, edges, output",
    [(4, [[2, 0], [2, 1], [1, 3]], [1, 1, 0, 2]), (3, [[1, 2], [2, 0]], [2, 0, 1])],
)
class TestSolution:
    def test_minEdgeReversals(self, n: int, edges: List[List[int]], output: List[int]):
        sc = Solution()
        assert (
            sc.minEdgeReversals(
                n,
                edges,
            )
            == output
        )
