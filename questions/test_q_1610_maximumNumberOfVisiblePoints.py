import pytest
from q_1610_maximumNumberOfVisiblePoints import Solution


@pytest.mark.parametrize(
    "points, angle, location, output",
    [
        ([[2, 1], [2, 2], [3, 3]], 90, [1, 1], 3),
        ([[2, 1], [2, 2], [3, 4], [1, 1]], 90, [1, 1], 4),
        ([[1, 0], [2, 1]], 13, [1, 1], 1),
    ],
)
class TestSolution:
    def test_visiblePoints(
        self, points: List[List[int]], angle: int, location: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.visiblePoints(
                points,
                angle,
                location,
            )
            == output
        )
