import pytest
from q_1560_mostVisitedSectorInACircularTrack import Solution


@pytest.mark.parametrize(
    "n, rounds, output",
    [
        (4, [1, 3, 1, 2], [1, 2]),
        (2, [2, 1, 2, 1, 2, 1, 2, 1, 2], [2]),
        (7, [1, 3, 5, 7], [1, 2, 3, 4, 5, 6, 7]),
    ],
)
class TestSolution:
    def test_mostVisited(self, n: int, rounds: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.mostVisited(
                n,
                rounds,
            )
            == output
        )
