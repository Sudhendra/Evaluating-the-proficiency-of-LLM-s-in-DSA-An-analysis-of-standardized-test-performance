import pytest
from q_1466_reorderRoutesToMakeAllPathsLeadToTheCityZero import Solution


@pytest.mark.parametrize(
    "n, connections, output",
    [
        (6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]], 3),
        (5, [[1, 0], [1, 2], [3, 2], [3, 4]], 2),
        (3, [[1, 0], [2, 0]], 0),
    ],
)
class TestSolution:
    def test_minReorder(self, n: int, connections: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minReorder(
                n,
                connections,
            )
            == output
        )
