import pytest
from q_0223_rectangleArea import Solution


@pytest.mark.parametrize(
    "ax1, ay1, ax2, ay2, bx1, by1, bx2, by2, output",
    [(-3, 0, 3, 4, 0, -1, 9, 2, 45), (-2, -2, 2, 2, -2, -2, 2, 2, 16)],
)
class TestSolution:
    def test_computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
        output: int,
    ):
        sc = Solution()
        assert (
            sc.computeArea(
                ax1,
                ay1,
                ax2,
                ay2,
                bx1,
                by1,
                bx2,
                by2,
            )
            == output
        )
