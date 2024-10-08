import pytest
from q_2857_countPairsOfPointsWithDistanceK import Solution


@pytest.mark.parametrize(
    "coordinates, k, output",
    [
        ([[1, 2], [4, 2], [1, 3], [5, 2]], 5, 2),
        ([[1, 3], [1, 3], [1, 3], [1, 3], [1, 3]], 0, 10),
    ],
)
class TestSolution:
    def test_countPairs(self, coordinates: List[List[int]], k: int, output: int):
        sc = Solution()
        assert (
            sc.countPairs(
                coordinates,
                k,
            )
            == output
        )
