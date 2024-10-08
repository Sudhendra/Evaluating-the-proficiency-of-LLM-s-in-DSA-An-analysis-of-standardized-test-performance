import pytest
from q_2374_nodeWithHighestEdgeScore import Solution


@pytest.mark.parametrize(
    "edges, output", [([1, 0, 0, 0, 0, 7, 7, 5], 7), ([2, 0, 0, 2], 0)]
)
class TestSolution:
    def test_edgeScore(self, edges: List[int], output: int):
        sc = Solution()
        assert (
            sc.edgeScore(
                edges,
            )
            == output
        )
