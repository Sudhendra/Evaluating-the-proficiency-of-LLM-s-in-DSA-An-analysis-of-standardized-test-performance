import pytest
from q_1319_numberOfOperationsToMakeNetworkConnected import Solution


@pytest.mark.parametrize(
    "n, connections, output",
    [
        (4, [[0, 1], [0, 2], [1, 2]], 1),
        (6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]], 2),
        (6, [[0, 1], [0, 2], [0, 3], [1, 2]], -1),
    ],
)
class TestSolution:
    def test_makeConnected(self, n: int, connections: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.makeConnected(
                n,
                connections,
            )
            == output
        )
