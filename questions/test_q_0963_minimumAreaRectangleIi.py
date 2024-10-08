import pytest
from q_0963_minimumAreaRectangleIi import Solution


@pytest.mark.parametrize(
    "points, output",
    [
        ([[1, 2], [2, 1], [1, 0], [0, 1]], 2.0),
        ([[0, 1], [2, 1], [1, 1], [1, 0], [2, 0]], 1.0),
        ([[0, 3], [1, 2], [3, 1], [1, 3], [2, 1]], 0),
    ],
)
class TestSolution:
    def test_minAreaFreeRect(self, points: List[List[int]], output: float):
        sc = Solution()
        assert (
            sc.minAreaFreeRect(
                points,
            )
            == output
        )
