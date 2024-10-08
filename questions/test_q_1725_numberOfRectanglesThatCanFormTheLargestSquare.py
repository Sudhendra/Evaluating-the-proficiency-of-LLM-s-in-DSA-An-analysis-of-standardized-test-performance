import pytest
from q_1725_numberOfRectanglesThatCanFormTheLargestSquare import Solution


@pytest.mark.parametrize(
    "rectangles, output",
    [([[5, 8], [3, 9], [5, 12], [16, 5]], 3), ([[2, 3], [3, 7], [4, 3], [3, 7]], 3)],
)
class TestSolution:
    def test_countGoodRectangles(self, rectangles: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.countGoodRectangles(
                rectangles,
            )
            == output
        )
