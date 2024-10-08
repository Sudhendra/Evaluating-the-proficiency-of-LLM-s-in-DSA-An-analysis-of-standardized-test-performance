import pytest
from q_0812_largestTriangleArea import Solution


@pytest.mark.parametrize(
    "points, output",
    [([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]], 2.0), ([[1, 0], [0, 0], [0, 1]], 0.5)],
)
class TestSolution:
    def test_largestTriangleArea(self, points: List[List[int]], output: float):
        sc = Solution()
        assert (
            sc.largestTriangleArea(
                points,
            )
            == output
        )
