import pytest
from q_0210_courseScheduleIi import Solution


@pytest.mark.parametrize(
    "numCourses, prerequisites, output",
    [
        (2, [[1, 0]], [0, 1]),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 2, 1, 3]),
        (1, [], [0]),
    ],
)
class TestSolution:
    def test_findOrder(
        self, numCourses: int, prerequisites: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.findOrder(
                numCourses,
                prerequisites,
            )
            == output
        )
