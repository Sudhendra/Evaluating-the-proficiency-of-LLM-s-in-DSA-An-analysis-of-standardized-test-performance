import pytest
from q_0785_isGraphBipartite import Solution


@pytest.mark.parametrize(
    "graph, output",
    [
        ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False),
        ([[1, 3], [0, 2], [1, 3], [0, 2]], True),
    ],
)
class TestSolution:
    def test_isBipartite(self, graph: List[List[int]], output: bool):
        sc = Solution()
        assert (
            sc.isBipartite(
                graph,
            )
            == output
        )
