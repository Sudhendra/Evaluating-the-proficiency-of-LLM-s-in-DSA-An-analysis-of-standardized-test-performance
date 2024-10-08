import pytest
from q_0214_shortestPalindrome import Solution


@pytest.mark.parametrize("s, output", [("aacecaaa", "aaacecaaa"), ("abcd", "dcbabcd")])
class TestSolution:
    def test_shortestPalindrome(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.shortestPalindrome(
                s,
            )
            == output
        )
