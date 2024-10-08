import pytest
from q_1489_findCriticalAndPseudoCriticalEdgesInMinimumSpanningTree import Solution


@pytest.mark.parametrize(
    "n, edges, output",
    [
        (
            5,
            [
                [0, 1, 1],
                [1, 2, 1],
                [2, 3, 2],
                [0, 3, 2],
                [0, 4, 3],
                [3, 4, 3],
                [1, 4, 6],
            ],
            [[0, 1], [2, 3, 4, 5]],
        ),
        (4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]], [[], [0, 1, 2, 3]]),
    ],
)
class TestSolution:
    def test_findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]], output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.findCriticalAndPseudoCriticalEdges(
                n,
                edges,
            )
            == output
        )
