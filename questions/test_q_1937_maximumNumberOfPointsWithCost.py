import pytest
from q_1937_maximumNumberOfPointsWithCost import Solution


@pytest.mark.parametrize(
    "points, output",
    [([[1, 2, 3], [1, 5, 1], [3, 1, 1]], 9), ([[1, 5], [2, 3], [4, 2]], 11)],
)
class TestSolution:
    def test_maxPoints(self, points: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maxPoints(
                points,
            )
            == output
        )
