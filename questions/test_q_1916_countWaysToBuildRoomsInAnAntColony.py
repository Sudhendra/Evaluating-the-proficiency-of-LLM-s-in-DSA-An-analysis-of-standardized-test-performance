import pytest
from q_1916_countWaysToBuildRoomsInAnAntColony import Solution


@pytest.mark.parametrize("prevRoom, output", [([-1, 0, 1], 1), ([-1, 0, 0, 1, 2], 6)])
class TestSolution:
    def test_waysToBuildRooms(self, prevRoom: List[int], output: int):
        sc = Solution()
        assert (
            sc.waysToBuildRooms(
                prevRoom,
            )
            == output
        )
