import pytest
from q_1616_splitTwoStringsToMakePalindrome import Solution


@pytest.mark.parametrize(
    "a, b, output",
    [("x", "y", True), ("xbdef", "xecab", False), ("ulacfd", "jizalu", True)],
)
class TestSolution:
    def test_checkPalindromeFormation(self, a: str, b: str, output: bool):
        sc = Solution()
        assert (
            sc.checkPalindromeFormation(
                a,
                b,
            )
            == output
        )
