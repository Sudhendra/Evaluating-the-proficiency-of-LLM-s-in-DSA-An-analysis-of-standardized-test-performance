import pytest
from q_1328_breakAPalindrome import Solution


@pytest.mark.parametrize("palindrome, output", [("abccba", "aaccba"), ("a", "")])
class TestSolution:
    def test_breakPalindrome(self, palindrome: str, output: str):
        sc = Solution()
        assert (
            sc.breakPalindrome(
                palindrome,
            )
            == output
        )
