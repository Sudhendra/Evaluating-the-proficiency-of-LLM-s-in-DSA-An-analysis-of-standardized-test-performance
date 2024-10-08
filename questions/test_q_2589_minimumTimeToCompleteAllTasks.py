import pytest
from q_2589_minimumTimeToCompleteAllTasks import Solution


@pytest.mark.parametrize(
    "tasks, output",
    [([[2, 3, 1], [4, 5, 1], [1, 5, 2]], 2), ([[1, 3, 2], [2, 5, 3], [5, 6, 2]], 4)],
)
class TestSolution:
    def test_findMinimumTime(self, tasks: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.findMinimumTime(
                tasks,
            )
            == output
        )
