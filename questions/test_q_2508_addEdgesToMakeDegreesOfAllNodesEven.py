import pytest
from q_2508_addEdgesToMakeDegreesOfAllNodesEven import Solution


@pytest.mark.parametrize(
    "n, edges, output",
    [
        (5, [[1, 2], [2, 3], [3, 4], [4, 2], [1, 4], [2, 5]], True),
        (4, [[1, 2], [3, 4]], True),
        (4, [[1, 2], [1, 3], [1, 4]], False),
    ],
)
class TestSolution:
    def test_isPossible(self, n: int, edges: List[List[int]], output: bool):
        sc = Solution()
        assert (
            sc.isPossible(
                n,
                edges,
            )
            == output
        )
