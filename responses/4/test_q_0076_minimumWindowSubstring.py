import pytest
from q_0076_minimumWindowSubstring import Solution


@pytest.mark.parametrize(
    "s, t, output", [("ADOBECODEBANC", "ABC", "BANC"), ("a", "a", "a"), ("a", "aa", "")]
)
class TestSolution:
    def test_minWindow(self, s: str, t: str, output: str):
        sc = Solution()
        assert (
            sc.minWindow(
                s,
                t,
            )
            == output
        )
