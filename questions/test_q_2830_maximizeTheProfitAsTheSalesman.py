import pytest
from q_2830_maximizeTheProfitAsTheSalesman import Solution


@pytest.mark.parametrize(
    "n, offers, output",
    [
        (5, [[0, 0, 1], [0, 2, 2], [1, 3, 2]], 3),
        (5, [[0, 0, 1], [0, 2, 10], [1, 3, 2]], 10),
    ],
)
class TestSolution:
    def test_maximizeTheProfit(self, n: int, offers: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maximizeTheProfit(
                n,
                offers,
            )
            == output
        )
