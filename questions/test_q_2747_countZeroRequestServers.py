import pytest
from q_2747_countZeroRequestServers import Solution


@pytest.mark.parametrize(
    "n, logs, x, queries, output",
    [
        (3, [[1, 3], [2, 6], [1, 5]], 5, [10, 11], [1, 2]),
        (3, [[2, 4], [2, 1], [1, 2], [3, 1]], 2, [3, 4], [0, 1]),
    ],
)
class TestSolution:
    def test_countServers(
        self,
        n: int,
        logs: List[List[int]],
        x: int,
        queries: List[int],
        output: List[int],
    ):
        sc = Solution()
        assert (
            sc.countServers(
                n,
                logs,
                x,
                queries,
            )
            == output
        )
