import pytest
from q_1976_numberOfWaysToArriveAtDestination import Solution


@pytest.mark.parametrize(
    "n, roads, output",
    [
        (
            7,
            [
                [0, 6, 7],
                [0, 1, 2],
                [1, 2, 3],
                [1, 3, 3],
                [6, 3, 3],
                [3, 5, 1],
                [6, 5, 1],
                [2, 5, 1],
                [0, 4, 5],
                [4, 6, 2],
            ],
            4,
        ),
        (2, [[1, 0, 10]], 1),
    ],
)
class TestSolution:
    def test_countPaths(self, n: int, roads: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.countPaths(
                n,
                roads,
            )
            == output
        )
