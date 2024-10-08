import pytest
from q_0409_longestPalindrome import Solution


@pytest.mark.parametrize("s, output", [("abccccdd", 7), ("a", 1)])
class TestSolution:
    def test_longestPalindrome(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.longestPalindrome(
                s,
            )
            == output
        )
