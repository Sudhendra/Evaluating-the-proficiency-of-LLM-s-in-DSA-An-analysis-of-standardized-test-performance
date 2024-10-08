import pytest
from q_0630_courseScheduleIii import Solution


@pytest.mark.parametrize(
    "courses, output",
    [
        ([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]], 3),
        ([[1, 2]], 1),
        ([[3, 2], [4, 3]], 0),
    ],
)
class TestSolution:
    def test_scheduleCourse(self, courses: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.scheduleCourse(
                courses,
            )
            == output
        )
