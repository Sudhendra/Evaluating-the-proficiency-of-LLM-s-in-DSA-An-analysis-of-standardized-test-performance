import pytest
from q_2008_maximumEarningsFromTaxi import Solution


@pytest.mark.parametrize(
    "n, rides, output",
    [
        (5, [[2, 5, 4], [1, 5, 1]], 7),
        (
            20,
            [[1, 6, 1], [3, 10, 2], [10, 12, 3], [11, 12, 2], [12, 15, 2], [13, 18, 1]],
            20,
        ),
    ],
)
class TestSolution:
    def test_maxTaxiEarnings(self, n: int, rides: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maxTaxiEarnings(
                n,
                rides,
            )
            == output
        )
