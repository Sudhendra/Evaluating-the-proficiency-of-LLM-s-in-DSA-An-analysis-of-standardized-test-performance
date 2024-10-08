import pytest
from q_0552_studentAttendanceRecordIi import Solution


@pytest.mark.parametrize("n, output", [(2, 8), (1, 3), (10101, 183236316)])
class TestSolution:
    def test_checkRecord(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.checkRecord(
                n,
            )
            == output
        )
