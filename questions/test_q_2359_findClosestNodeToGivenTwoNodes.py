import pytest
from q_2359_findClosestNodeToGivenTwoNodes import Solution


@pytest.mark.parametrize(
    "edges, node1, node2, output", [([2, 2, 3, -1], 0, 1, 2), ([1, 2, -1], 0, 2, 2)]
)
class TestSolution:
    def test_closestMeetingNode(
        self, edges: List[int], node1: int, node2: int, output: int
    ):
        sc = Solution()
        assert (
            sc.closestMeetingNode(
                edges,
                node1,
                node2,
            )
            == output
        )
