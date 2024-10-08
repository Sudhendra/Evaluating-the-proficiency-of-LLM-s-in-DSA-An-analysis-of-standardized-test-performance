import pytest
from q_1266_minimumTimeVisitingAllPoints import Solution


@pytest.mark.parametrize(
    "points, output", [([[1, 1], [3, 4], [-1, 0]], 7), ([[3, 2], [-2, 2]], 5)]
)
class TestSolution:
    def test_minTimeToVisitAllPoints(self, points: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minTimeToVisitAllPoints(
                points,
            )
            == output
        )
