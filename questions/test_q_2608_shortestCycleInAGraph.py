import pytest
from q_2608_shortestCycleInAGraph import Solution


@pytest.mark.parametrize(
    "n, edges, output",
    [
        (7, [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]], 3),
        (4, [[0, 1], [0, 2]], -1),
    ],
)
class TestSolution:
    def test_findShortestCycle(self, n: int, edges: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.findShortestCycle(
                n,
                edges,
            )
            == output
        )
