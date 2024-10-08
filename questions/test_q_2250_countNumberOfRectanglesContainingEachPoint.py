import pytest
from q_2250_countNumberOfRectanglesContainingEachPoint import Solution


@pytest.mark.parametrize(
    "rectangles, points, output",
    [
        ([[1, 2], [2, 3], [2, 5]], [[2, 1], [1, 4]], [2, 1]),
        ([[1, 1], [2, 2], [3, 3]], [[1, 3], [1, 1]], [1, 3]),
    ],
)
class TestSolution:
    def test_countRectangles(
        self, rectangles: List[List[int]], points: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.countRectangles(
                rectangles,
                points,
            )
            == output
        )
