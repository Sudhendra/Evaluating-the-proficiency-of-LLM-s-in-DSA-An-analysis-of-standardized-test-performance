import pytest
from q_0310_minimumHeightTrees import Solution


@pytest.mark.parametrize(
    "n, edges, output",
    [
        (4, [[1, 0], [1, 2], [1, 3]], [1]),
        (6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]], [3, 4]),
    ],
)
class TestSolution:
    def test_findMinHeightTrees(
        self, n: int, edges: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.findMinHeightTrees(
                n,
                edges,
            )
            == output
        )
