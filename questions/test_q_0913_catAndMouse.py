import pytest
from q_0913_catAndMouse import Solution


@pytest.mark.parametrize(
    "graph, output",
    [
        ([[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]], 0),
        ([[1, 3], [0], [3], [0, 2]], 1),
    ],
)
class TestSolution:
    def test_catMouseGame(self, graph: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.catMouseGame(
                graph,
            )
            == output
        )
