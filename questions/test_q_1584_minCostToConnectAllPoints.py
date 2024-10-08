import pytest
from q_1584_minCostToConnectAllPoints import Solution


@pytest.mark.parametrize(
    "points, output",
    [
        ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20),
        ([[3, 12], [-2, 5], [-4, 1]], 18),
    ],
)
class TestSolution:
    def test_minCostConnectPoints(self, points: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minCostConnectPoints(
                points,
            )
            == output
        )
