import pytest
from q_2285_maximumTotalImportanceOfRoads import Solution


@pytest.mark.parametrize(
    "n, roads, output",
    [
        (5, [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]], 43),
        (5, [[0, 3], [2, 4], [1, 3]], 20),
    ],
)
class TestSolution:
    def test_maximumImportance(self, n: int, roads: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maximumImportance(
                n,
                roads,
            )
            == output
        )
