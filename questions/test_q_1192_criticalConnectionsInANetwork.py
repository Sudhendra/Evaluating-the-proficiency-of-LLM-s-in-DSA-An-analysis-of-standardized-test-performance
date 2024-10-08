import pytest
from q_1192_criticalConnectionsInANetwork import Solution


@pytest.mark.parametrize(
    "n, connections, output",
    [(4, [[0, 1], [1, 2], [2, 0], [1, 3]], [[1, 3]]), (2, [[0, 1]], [[0, 1]])],
)
class TestSolution:
    def test_criticalConnections(
        self, n: int, connections: List[List[int]], output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.criticalConnections(
                n,
                connections,
            )
            == output
        )
