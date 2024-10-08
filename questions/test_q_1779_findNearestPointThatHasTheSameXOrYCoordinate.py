import pytest
from q_1779_findNearestPointThatHasTheSameXOrYCoordinate import Solution


@pytest.mark.parametrize(
    "x, y, points, output",
    [
        (3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]], 2),
        (3, 4, [[3, 4]], 0),
        (3, 4, [[2, 3]], -1),
    ],
)
class TestSolution:
    def test_nearestValidPoint(
        self, x: int, y: int, points: List[List[int]], output: int
    ):
        sc = Solution()
        assert (
            sc.nearestValidPoint(
                x,
                y,
                points,
            )
            == output
        )
