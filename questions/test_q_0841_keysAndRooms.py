import pytest
from q_0841_keysAndRooms import Solution


@pytest.mark.parametrize(
    "rooms, output",
    [([[1], [2], [3], []], True), ([[1, 3], [3, 0, 1], [2], [0]], False)],
)
class TestSolution:
    def test_canVisitAllRooms(self, rooms: List[List[int]], output: bool):
        sc = Solution()
        assert (
            sc.canVisitAllRooms(
                rooms,
            )
            == output
        )
