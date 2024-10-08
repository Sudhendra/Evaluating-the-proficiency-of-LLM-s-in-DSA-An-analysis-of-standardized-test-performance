import pytest
from q_1185_dayOfTheWeek import Solution


@pytest.mark.parametrize(
    "day, month, year, output",
    [(31, 8, 2019, "Saturday"), (18, 7, 1999, "Sunday"), (15, 8, 1993, "Sunday")],
)
class TestSolution:
    def test_dayOfTheWeek(self, day: int, month: int, year: int, output: str):
        sc = Solution()
        assert (
            sc.dayOfTheWeek(
                day,
                month,
                year,
            )
            == output
        )
