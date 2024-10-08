import pytest
from q_2437_numberOfValidClockTimes import Solution


@pytest.mark.parametrize(
    "time, output", [("?5:00", 2), ("0?:0?", 100), ("??:??", 1440)]
)
class TestSolution:
    def test_countTime(self, time: str, output: int):
        sc = Solution()
        assert (
            sc.countTime(
                time,
            )
            == output
        )
