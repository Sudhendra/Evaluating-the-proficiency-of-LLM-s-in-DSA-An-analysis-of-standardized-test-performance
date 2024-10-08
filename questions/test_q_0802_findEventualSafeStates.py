import pytest
from q_0802_findEventualSafeStates import Solution


@pytest.mark.parametrize(
    "graph, output",
    [
        ([[1, 2], [2, 3], [5], [0], [5], [], []], [2, 4, 5, 6]),
        ([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []], [4]),
    ],
)
class TestSolution:
    def test_eventualSafeNodes(self, graph: List[List[int]], output: List[int]):
        sc = Solution()
        assert (
            sc.eventualSafeNodes(
                graph,
            )
            == output
        )
