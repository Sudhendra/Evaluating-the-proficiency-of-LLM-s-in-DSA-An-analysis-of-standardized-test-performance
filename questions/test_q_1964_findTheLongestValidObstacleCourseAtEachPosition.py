import pytest
from q_1964_findTheLongestValidObstacleCourseAtEachPosition import Solution


@pytest.mark.parametrize(
    "obstacles, output",
    [
        ([1, 2, 3, 2], [1, 2, 3, 3]),
        ([2, 2, 1], [1, 2, 1]),
        ([3, 1, 5, 6, 4, 2], [1, 1, 2, 3, 2, 2]),
    ],
)
class TestSolution:
    def test_longestObstacleCourseAtEachPosition(
        self, obstacles: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.longestObstacleCourseAtEachPosition(
                obstacles,
            )
            == output
        )
