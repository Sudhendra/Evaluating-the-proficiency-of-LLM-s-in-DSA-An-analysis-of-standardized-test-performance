import pytest
from q_0797_allPathsFromSourceToTarget import Solution


@pytest.mark.parametrize(
    "graph, output",
    [
        ([[1, 2], [3], [3], []], [[0, 1, 3], [0, 2, 3]]),
        (
            [[4, 3, 1], [3, 2, 4], [3], [4], []],
            [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]],
        ),
    ],
)
class TestSolution:
    def test_allPathsSourceTarget(
        self, graph: List[List[int]], output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.allPathsSourceTarget(
                graph,
            )
            == output
        )
