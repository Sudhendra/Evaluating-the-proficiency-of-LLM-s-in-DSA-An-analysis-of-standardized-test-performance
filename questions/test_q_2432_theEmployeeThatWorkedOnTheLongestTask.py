import pytest
from q_2432_theEmployeeThatWorkedOnTheLongestTask import Solution


@pytest.mark.parametrize(
    "n, logs, output",
    [
        (10, [[0, 3], [2, 5], [0, 9], [1, 15]], 1),
        (26, [[1, 1], [3, 7], [2, 12], [7, 17]], 3),
        (2, [[0, 10], [1, 20]], 0),
    ],
)
class TestSolution:
    def test_hardestWorker(self, n: int, logs: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.hardestWorker(
                n,
                logs,
            )
            == output
        )
