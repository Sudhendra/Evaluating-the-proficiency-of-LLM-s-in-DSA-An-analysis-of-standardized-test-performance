import pytest
from q_1615_maximalNetworkRank import Solution


@pytest.mark.parametrize(
    "n, roads, output",
    [
        (4, [[0, 1], [0, 3], [1, 2], [1, 3]], 4),
        (5, [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]], 5),
        (8, [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]], 5),
    ],
)
class TestSolution:
    def test_maximalNetworkRank(self, n: int, roads: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maximalNetworkRank(
                n,
                roads,
            )
            == output
        )
