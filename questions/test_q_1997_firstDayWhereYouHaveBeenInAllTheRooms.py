import pytest
from q_1997_firstDayWhereYouHaveBeenInAllTheRooms import Solution


@pytest.mark.parametrize(
    "nextVisit, output", [([0, 0], 2), ([0, 0, 2], 6), ([0, 1, 2, 0], 6)]
)
class TestSolution:
    def test_firstDayBeenInAllRooms(self, nextVisit: List[int], output: int):
        sc = Solution()
        assert (
            sc.firstDayBeenInAllRooms(
                nextVisit,
            )
            == output
        )
