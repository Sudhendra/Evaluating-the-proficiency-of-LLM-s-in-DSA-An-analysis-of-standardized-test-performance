import pytest
from q_0944_deleteColumnsToMakeSorted import Solution


@pytest.mark.parametrize(
    "strs, output",
    [(["cba", "daf", "ghi"], 1), (["a", "b"], 0), (["zyx", "wvu", "tsr"], 3)],
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
