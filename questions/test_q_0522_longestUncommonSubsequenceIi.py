import pytest
from q_0522_longestUncommonSubsequenceIi import Solution


@pytest.mark.parametrize(
    "strs, output", [(["aba", "cdc", "eae"], 3), (["aaa", "aaa", "aa"], -1)]
)
class TestSolution:
    def test_findLUSlength(self, strs: List[str], output: int):
        sc = Solution()
        assert (
            sc.findLUSlength(
                strs,
            )
            == output
        )
