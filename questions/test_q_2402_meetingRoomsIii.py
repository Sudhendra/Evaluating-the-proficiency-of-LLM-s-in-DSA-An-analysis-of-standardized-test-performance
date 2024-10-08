import pytest
from q_2402_meetingRoomsIii import Solution


@pytest.mark.parametrize(
    "n, meetings, output",
    [
        (2, [[0, 10], [1, 5], [2, 7], [3, 4]], 0),
        (3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]], 1),
    ],
)
class TestSolution:
    def test_mostBooked(self, n: int, meetings: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.mostBooked(
                n,
                meetings,
            )
            == output
        )
