import pytest
from q_0207_courseSchedule import Solution


@pytest.mark.parametrize(
    "numCourses, prerequisites, output",
    [(2, [[1, 0]], True), (2, [[1, 0], [0, 1]], False)],
)
class TestSolution:
    def test_canFinish(
        self, numCourses: int, prerequisites: List[List[int]], output: bool
    ):
        sc = Solution()
        assert (
            sc.canFinish(
                numCourses,
                prerequisites,
            )
            == output
        )
