import pytest
from q_2365_taskSchedulerIi import Solution


@pytest.mark.parametrize(
    "tasks, space, output", [([1, 2, 1, 2, 3, 1], 3, 9), ([5, 8, 8, 5], 2, 6)]
)
class TestSolution:
    def test_taskSchedulerII(self, tasks: List[int], space: int, output: int):
        sc = Solution()
        assert (
            sc.taskSchedulerII(
                tasks,
                space,
            )
            == output
        )
