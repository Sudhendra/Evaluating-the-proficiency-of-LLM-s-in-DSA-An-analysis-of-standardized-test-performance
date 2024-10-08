import pytest
from q_0960_deleteColumnsToMakeSortedIii import Solution


@pytest.mark.parametrize(
    "strs, output",
    [(["babca", "bbazb"], 3), (["edcba"], 4), (["ghi", "def", "abc"], 0)],
)
class TestSolution:
    def test_minDeletionSize(self, strs: List[str], output: int):
        sc = Solution()
        assert (
            sc.minDeletionSize(
                strs,
            )
            == output
        )
