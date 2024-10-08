import pytest
from q_0005_longestPalindromicSubstring import Solution


@pytest.mark.parametrize("s, output", [("babad", "bab"), ("cbbd", "bb")])
class TestSolution:
    def test_longestPalindrome(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.longestPalindrome(
                s,
            )
            == output
        )
