import pytest
from q_0787_cheapestFlightsWithinKStops import Solution


@pytest.mark.parametrize(
    "n, flights, src, dst, k, output",
    [
        (
            4,
            [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
            0,
            3,
            1,
            700,
        ),
        (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200),
        (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0, 500),
    ],
)
class TestSolution:
    def test_findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int, output: int
    ):
        sc = Solution()
        assert (
            sc.findCheapestPrice(
                n,
                flights,
                src,
                dst,
                k,
            )
            == output
        )
