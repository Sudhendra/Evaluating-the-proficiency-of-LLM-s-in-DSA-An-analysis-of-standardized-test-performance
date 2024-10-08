import pytest
from q_1857_largestColorValueInADirectedGraph import Solution


@pytest.mark.parametrize(
    "colors, edges, output",
    [("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]], 3), ("a", [[0, 0]], -1)],
)
class TestSolution:
    def test_largestPathValue(self, colors: str, edges: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.largestPathValue(
                colors,
                edges,
            )
            == output
        )
