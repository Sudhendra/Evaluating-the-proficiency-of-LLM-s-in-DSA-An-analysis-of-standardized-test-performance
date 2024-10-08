import pytest
from q_1507_reformatDate import Solution


@pytest.mark.parametrize(
    "date, output",
    [
        ("20th Oct 2052", "2052-10-20"),
        ("6th Jun 1933", "1933-06-06"),
        ("26th May 1960", "1960-05-26"),
    ],
)
class TestSolution:
    def test_reformatDate(self, date: str, output: str):
        sc = Solution()
        assert (
            sc.reformatDate(
                date,
            )
            == output
        )
