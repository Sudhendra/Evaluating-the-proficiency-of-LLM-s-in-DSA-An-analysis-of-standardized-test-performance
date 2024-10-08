import pytest
from q_1499_maxValueOfEquation import Solution


@pytest.mark.parametrize(
    "points, k, output",
    [([[1, 3], [2, 0], [5, 10], [6, -10]], 1, 4), ([[0, 0], [3, 0], [9, 2]], 3, 3)],
)
class TestSolution:
    def test_findMaxValueOfEquation(self, points: List[List[int]], k: int, output: int):
        sc = Solution()
        assert (
            sc.findMaxValueOfEquation(
                points,
                k,
            )
            == output
        )
