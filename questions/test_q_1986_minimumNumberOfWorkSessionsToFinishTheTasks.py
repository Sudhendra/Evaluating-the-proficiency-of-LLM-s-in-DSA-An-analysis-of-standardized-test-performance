import pytest
from q_1986_minimumNumberOfWorkSessionsToFinishTheTasks import Solution


@pytest.mark.parametrize(
    "tasks, sessionTime, output",
    [([1, 2, 3], 3, 2), ([3, 1, 3, 1, 1], 8, 2), ([1, 2, 3, 4, 5], 15, 1)],
)
class TestSolution:
    def test_minSessions(self, tasks: List[int], sessionTime: int, output: int):
        sc = Solution()
        assert (
            sc.minSessions(
                tasks,
                sessionTime,
            )
            == output
        )
