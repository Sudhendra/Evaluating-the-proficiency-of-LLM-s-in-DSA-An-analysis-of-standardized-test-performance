import pytest
from q_0685_redundantConnectionIi import Solution


@pytest.mark.parametrize(
    "edges, output",
    [
        ([[1, 2], [1, 3], [2, 3]], [2, 3]),
        ([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]], [4, 1]),
    ],
)
class TestSolution:
    def test_findRedundantDirectedConnection(
        self, edges: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.findRedundantDirectedConnection(
                edges,
            )
            == output
        )
