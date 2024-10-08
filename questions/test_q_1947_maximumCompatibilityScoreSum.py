import pytest
from q_1947_maximumCompatibilityScoreSum import Solution


@pytest.mark.parametrize(
    "students, mentors, output",
    [
        ([[1, 1, 0], [1, 0, 1], [0, 0, 1]], [[1, 0, 0], [0, 0, 1], [1, 1, 0]], 8),
        ([[0, 0], [0, 0], [0, 0]], [[1, 1], [1, 1], [1, 1]], 0),
    ],
)
class TestSolution:
    def test_maxCompatibilitySum(
        self, students: List[List[int]], mentors: List[List[int]], output: int
    ):
        sc = Solution()
        assert (
            sc.maxCompatibilitySum(
                students,
                mentors,
            )
            == output
        )
