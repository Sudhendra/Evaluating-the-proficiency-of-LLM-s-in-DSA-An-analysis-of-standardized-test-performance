import pytest
from q_0551_studentAttendanceRecordI import Solution


@pytest.mark.parametrize("s, output", [("PPALLP", True), ("PPALLL", False)])
class TestSolution:
    def test_checkRecord(self, s: str, output: bool):
        sc = Solution()
        assert (
            sc.checkRecord(
                s,
            )
            == output
        )
