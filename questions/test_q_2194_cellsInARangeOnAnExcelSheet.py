import pytest
from q_2194_cellsInARangeOnAnExcelSheet import Solution


@pytest.mark.parametrize(
    "s, output",
    [
        ("K1:L2", ["K1", "K2", "L1", "L2"]),
        ("A1:F1", ["A1", "B1", "C1", "D1", "E1", "F1"]),
    ],
)
class TestSolution:
    def test_cellsInRange(self, s: str, output: List[str]):
        sc = Solution()
        assert (
            sc.cellsInRange(
                s,
            )
            == output
        )
