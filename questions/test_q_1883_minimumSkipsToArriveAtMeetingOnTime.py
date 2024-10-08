import pytest
from q_1883_minimumSkipsToArriveAtMeetingOnTime import Solution


@pytest.mark.parametrize(
    "dist, speed, hoursBefore, output",
    [([1, 3, 2], 4, 2, 1), ([7, 3, 5, 5], 2, 10, 2), ([7, 3, 5, 5], 1, 10, -1)],
)
class TestSolution:
    def test_minSkips(self, dist: List[int], speed: int, hoursBefore: int, output: int):
        sc = Solution()
        assert (
            sc.minSkips(
                dist,
                speed,
                hoursBefore,
            )
            == output
        )
