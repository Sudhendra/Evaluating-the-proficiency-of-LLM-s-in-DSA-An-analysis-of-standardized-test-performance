import pytest
from q_1334_findTheCityWithTheSmallestNumberOfNeighborsAtAThresholdDistance import (
    Solution,
)


@pytest.mark.parametrize(
    "n, edges, distanceThreshold, output",
    [
        (4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4, 3),
        (5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2, 0),
    ],
)
class TestSolution:
    def test_findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int, output: int
    ):
        sc = Solution()
        assert (
            sc.findTheCity(
                n,
                edges,
                distanceThreshold,
            )
            == output
        )
