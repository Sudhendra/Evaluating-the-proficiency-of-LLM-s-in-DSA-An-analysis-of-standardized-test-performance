import pytest
from q_1817_findingTheUsersActiveMinutes import Solution


@pytest.mark.parametrize(
    "logs, k, output",
    [
        ([[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]], 5, [0, 2, 0, 0, 0]),
        ([[1, 1], [2, 2], [2, 3]], 4, [1, 1, 0, 0]),
    ],
)
class TestSolution:
    def test_findingUsersActiveMinutes(
        self, logs: List[List[int]], k: int, output: List[int]
    ):
        sc = Solution()
        assert (
            sc.findingUsersActiveMinutes(
                logs,
                k,
            )
            == output
        )
