import pytest
from q_0125_validPalindrome import Solution


@pytest.mark.parametrize(
    "s, output",
    [("A man, a plan, a canal: Panama", True), ("race a car", False), (" ", True)],
)
class TestSolution:
    def test_isPalindrome(self, s: str, output: bool):
        sc = Solution()
        assert (
            sc.isPalindrome(
                s,
            )
            == output
        )
