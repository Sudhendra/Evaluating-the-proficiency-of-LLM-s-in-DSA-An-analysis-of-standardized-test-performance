import pytest
from q_2920_maximumPointsAfterCollectingCoinsFromAllNodes import Solution


@pytest.mark.parametrize(
    "edges, coins, k, output",
    [
        ([[0, 1], [1, 2], [2, 3]], [10, 10, 3, 3], 5, 11),
        ([[0, 1], [0, 2]], [8, 4, 4], 0, 16),
    ],
)
class TestSolution:
    def test_maximumPoints(
        self, edges: List[List[int]], coins: List[int], k: int, output: int
    ):
        sc = Solution()
        assert (
            sc.maximumPoints(
                edges,
                coins,
                k,
            )
            == output
        )
