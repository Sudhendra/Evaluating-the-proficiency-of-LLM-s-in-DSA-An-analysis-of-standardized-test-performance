import pytest
from q_1882_processTasksUsingServers import Solution


@pytest.mark.parametrize(
    "servers, tasks, output",
    [
        ([3, 3, 2], [1, 2, 3, 2, 1, 2], [2, 2, 0, 2, 1, 2]),
        ([5, 1, 4, 3, 2], [2, 1, 2, 4, 5, 2, 1], [1, 4, 1, 4, 1, 3, 2]),
    ],
)
class TestSolution:
    def test_assignTasks(self, servers: List[int], tasks: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.assignTasks(
                servers,
                tasks,
            )
            == output
        )
