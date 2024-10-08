import pytest
from q_2699_modifyGraphEdgeWeights import Solution


@pytest.mark.parametrize(
    "n, edges, source, destination, target, output",
    [
        (
            5,
            [[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]],
            0,
            1,
            5,
            [[4, 1, 1], [2, 0, 1], [0, 3, 3], [4, 3, 1]],
        ),
        (3, [[0, 1, -1], [0, 2, 5]], 0, 2, 6, []),
        (
            4,
            [[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, -1]],
            0,
            2,
            6,
            [[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, 1]],
        ),
    ],
)
class TestSolution:
    def test_modifiedGraphEdges(
        self,
        n: int,
        edges: List[List[int]],
        source: int,
        destination: int,
        target: int,
        output: List[List[int]],
    ):
        sc = Solution()
        assert (
            sc.modifiedGraphEdges(
                n,
                edges,
                source,
                destination,
                target,
            )
            == output
        )
