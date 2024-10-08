import pytest
from q_0391_perfectRectangle import Solution


@pytest.mark.parametrize(
    "rectangles, output",
    [
        ([[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]], True),
        ([[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]], False),
        ([[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [2, 2, 4, 4]], False),
    ],
)
class TestSolution:
    def test_isRectangleCover(self, rectangles: List[List[int]], output: bool):
        sc = Solution()
        assert (
            sc.isRectangleCover(
                rectangles,
            )
            == output
        )
