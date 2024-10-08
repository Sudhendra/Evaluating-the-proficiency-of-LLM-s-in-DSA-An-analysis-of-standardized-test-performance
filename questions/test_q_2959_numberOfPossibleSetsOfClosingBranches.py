import pytest
from q_2959_numberOfPossibleSetsOfClosingBranches import Solution


@pytest.mark.parametrize(
    "n, maxDistance, roads, output",
    [
        (3, 5, [[0, 1, 2], [1, 2, 10], [0, 2, 10]], 5),
        (3, 5, [[0, 1, 20], [0, 1, 10], [1, 2, 2], [0, 2, 2]], 7),
        (1, 10, [], 2),
    ],
)
class TestSolution:
    def test_numberOfSets(
        self, n: int, maxDistance: int, roads: List[List[int]], output: int
    ):
        sc = Solution()
        assert (
            sc.numberOfSets(
                n,
                maxDistance,
                roads,
            )
            == output
        )
