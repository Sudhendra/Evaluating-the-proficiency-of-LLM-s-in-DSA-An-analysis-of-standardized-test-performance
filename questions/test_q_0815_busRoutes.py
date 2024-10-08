import pytest
from q_0815_busRoutes import Solution


@pytest.mark.parametrize(
    "routes, source, target, output",
    [
        ([[1, 2, 7], [3, 6, 7]], 1, 6, 2),
        ([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12, -1),
    ],
)
class TestSolution:
    def test_numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int, output: int
    ):
        sc = Solution()
        assert (
            sc.numBusesToDestination(
                routes,
                source,
                target,
            )
            == output
        )
