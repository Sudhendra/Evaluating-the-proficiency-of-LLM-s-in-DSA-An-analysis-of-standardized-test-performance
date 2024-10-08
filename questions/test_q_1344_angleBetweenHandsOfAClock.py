import pytest
from q_1344_angleBetweenHandsOfAClock import Solution


@pytest.mark.parametrize(
    "hour, minutes, output", [(12, 30, 165), (3, 30, 75), (3, 15, 7.5)]
)
class TestSolution:
    def test_angleClock(self, hour: int, minutes: int, output: float):
        sc = Solution()
        assert (
            sc.angleClock(
                hour,
                minutes,
            )
            == output
        )
