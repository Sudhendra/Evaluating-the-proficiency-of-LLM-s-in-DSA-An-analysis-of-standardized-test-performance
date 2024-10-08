import pytest
from q_2244_minimumRoundsToCompleteAllTasks import Solution


@pytest.mark.parametrize(
    "tasks, output", [([2, 2, 3, 3, 2, 4, 4, 4, 4, 4], 4), ([2, 3, 3], -1)]
)
class TestSolution:
    def test_minimumRounds(self, tasks: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumRounds(
                tasks,
            )
            == output
        )
