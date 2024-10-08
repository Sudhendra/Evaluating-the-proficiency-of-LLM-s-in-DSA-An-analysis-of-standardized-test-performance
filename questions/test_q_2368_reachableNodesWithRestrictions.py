import pytest
from q_2368_reachableNodesWithRestrictions import Solution


@pytest.mark.parametrize(
    "n, edges, restricted, output",
    [
        (7, [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], [4, 5], 4),
        (7, [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]], [4, 2, 1], 3),
    ],
)
class TestSolution:
    def test_reachableNodes(
        self, n: int, edges: List[List[int]], restricted: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.reachableNodes(
                n,
                edges,
                restricted,
            )
            == output
        )
