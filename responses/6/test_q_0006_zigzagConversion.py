import pytest
from q_0006_zigzagConversion import Solution


@pytest.mark.parametrize(
    "s, numRows, output",
    [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
    ],
)
class TestSolution:
    def test_convert(self, s: str, numRows: int, output: str):
        sc = Solution()
        assert (
            sc.convert(
                s,
                numRows,
            )
            == output
        )
