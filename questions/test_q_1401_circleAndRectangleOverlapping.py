import pytest
from q_1401_circleAndRectangleOverlapping import Solution


@pytest.mark.parametrize(
    "radius, xCenter, yCenter, x1, y1, x2, y2, output",
    [
        (1, 0, 0, 1, -1, 3, 1, True),
        (1, 1, 1, 1, -3, 2, -1, False),
        (1, 0, 0, -1, 0, 0, 1, True),
    ],
)
class TestSolution:
    def test_checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        output: bool,
    ):
        sc = Solution()
        assert (
            sc.checkOverlap(
                radius,
                xCenter,
                yCenter,
                x1,
                y1,
                x2,
                y2,
            )
            == output
        )
