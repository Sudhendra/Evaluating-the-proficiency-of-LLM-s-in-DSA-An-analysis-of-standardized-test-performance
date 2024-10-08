import pytest
from q_0521_longestUncommonSubsequenceI import Solution


@pytest.mark.parametrize(
    "a, b, output", [("aba", "cdc", 3), ("aaa", "bbb", 3), ("aaa", "aaa", -1)]
)
class TestSolution:
    def test_findLUSlength(self, a: str, b: str, output: int):
        sc = Solution()
        assert (
            sc.findLUSlength(
                a,
                b,
            )
            == output
        )
