import pytest
from q_2050_parallelCoursesIii import Solution


@pytest.mark.parametrize(
    "n, relations, time, output",
    [
        (3, [[1, 3], [2, 3]], [3, 2, 5], 8),
        (5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5], 12),
    ],
)
class TestSolution:
    def test_minimumTime(
        self, n: int, relations: List[List[int]], time: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.minimumTime(
                n,
                relations,
                time,
            )
            == output
        )
