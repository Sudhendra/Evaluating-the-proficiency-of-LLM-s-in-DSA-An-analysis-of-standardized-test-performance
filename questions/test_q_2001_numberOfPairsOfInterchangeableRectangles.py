import pytest
from q_2001_numberOfPairsOfInterchangeableRectangles import Solution


@pytest.mark.parametrize(
    "rectangles, output",
    [([[4, 8], [3, 6], [10, 20], [15, 30]], 6), ([[4, 5], [7, 8]], 0)],
)
class TestSolution:
    def test_interchangeableRectangles(self, rectangles: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.interchangeableRectangles(
                rectangles,
            )
            == output
        )
