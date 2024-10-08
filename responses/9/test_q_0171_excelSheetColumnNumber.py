import pytest
from q_0171_excelSheetColumnNumber import Solution


@pytest.mark.parametrize("columnTitle, output", [("A", 1), ("AB", 28), ("ZY", 701)])
class TestSolution:
    def test_titleToNumber(self, columnTitle: str, output: int):
        sc = Solution()
        assert (
            sc.titleToNumber(
                columnTitle,
            )
            == output
        )
