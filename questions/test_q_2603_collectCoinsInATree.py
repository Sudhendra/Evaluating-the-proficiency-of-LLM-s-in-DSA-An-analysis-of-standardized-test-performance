import pytest
from q_2603_collectCoinsInATree import Solution


@pytest.mark.parametrize(
    "coins, edges, output",
    [
        ([1, 0, 0, 0, 0, 1], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]], 2),
        (
            [0, 0, 0, 1, 1, 0, 0, 1],
            [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [5, 6], [5, 7]],
            2,
        ),
    ],
)
class TestSolution:
    def test_collectTheCoins(
        self, coins: List[int], edges: List[List[int]], output: int
    ):
        sc = Solution()
        assert (
            sc.collectTheCoins(
                coins,
                edges,
            )
            == output
        )
