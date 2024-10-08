import pytest
from q_1163_lastSubstringInLexicographicalOrder import Solution


@pytest.mark.parametrize("s, output", [("abab", "bab"), ("leetcode", "tcode")])
class TestSolution:
    def test_lastSubstring(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.lastSubstring(
                s,
            )
            == output
        )
