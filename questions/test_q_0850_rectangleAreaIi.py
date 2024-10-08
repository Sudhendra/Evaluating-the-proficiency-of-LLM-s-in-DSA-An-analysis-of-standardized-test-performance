import pytest
from q_0850_rectangleAreaIi import Solution


@pytest.mark.parametrize(
    "rectangles, output",
    [
        ([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]], 6),
        ([[0, 0, 1000000000, 1000000000]], 49),
    ],
)
class TestSolution:
    def test_rectangleArea(self, rectangles: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.rectangleArea(
                rectangles,
            )
            == output
        )
