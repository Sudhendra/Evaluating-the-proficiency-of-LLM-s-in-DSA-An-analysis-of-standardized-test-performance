import pytest
from q_2192_allAncestorsOfANodeInADirectedAcyclicGraph import Solution


@pytest.mark.parametrize(
    "n, edgeList, output",
    [
        (
            8,
            [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]],
            [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]],
        ),
        (
            5,
            [
                [0, 1],
                [0, 2],
                [0, 3],
                [0, 4],
                [1, 2],
                [1, 3],
                [1, 4],
                [2, 3],
                [2, 4],
                [3, 4],
            ],
            [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]],
        ),
    ],
)
class TestSolution:
    def test_getAncestors(
        self, n: int, edges: List[List[int]], output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.getAncestors(
                n,
                edgeList,
            )
            == output
        )
