import pytest
from q_0849_maximizeDistanceToClosestPerson import Solution


@pytest.mark.parametrize(
    "seats, output", [([1, 0, 0, 0, 1, 0, 1], 2), ([1, 0, 0, 0], 3), ([0, 1], 1)]
)
class TestSolution:
    def test_maxDistToClosest(self, seats: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxDistToClosest(
                seats,
            )
            == output
        )
