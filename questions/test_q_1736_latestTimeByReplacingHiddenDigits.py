import pytest
from q_1736_latestTimeByReplacingHiddenDigits import Solution


@pytest.mark.parametrize(
    "time, output", [("2?:?0", "23:50"), ("0?:3?", "09:39"), ("1?:22", "19:22")]
)
class TestSolution:
    def test_maximumTime(self, time: str, output: str):
        sc = Solution()
        assert (
            sc.maximumTime(
                time,
            )
            == output
        )
